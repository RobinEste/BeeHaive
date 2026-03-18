"""Calibrate the Gemini taxonomy mapper against seed.py ground truth.

This is a consistency check: it verifies that the Gemini classifier
reproduces the hand-curated labels from seed.py. The ground truth is
NOT an independent validation set — it is the same seed data used to
populate the knowledge graph.

This script bypasses scan_pii() — seed content is public academic
material without PII. This assumption is the module invariant.
"""

import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Add backend to Python path and load .env before app imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

from app.graph.seed import BUILDING_BLOCKS, GUARDRAILS, KNOWLEDGE_ITEMS  # noqa: E402
from app.ingestion.llm import (  # noqa: E402
    _BUILDING_BLOCKS as LLM_BUILDING_BLOCKS,
    _GUARDRAILS as LLM_GUARDRAILS,
    classify_text,
)

# Rate limiting: 4 sec between calls (Gemini free tier = 15 RPM)
RATE_LIMIT_SECONDS = 4

# Threshold levels for reporting
THRESHOLDS = [0.0, 0.7]

# Exit-code threshold for normatieve metrics
EXIT_THRESHOLD = 0.70


def get_git_sha() -> str:
    """Get current git short SHA."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


def pre_check_taxonomy() -> bool:
    """Verify BB/GR names match between seed.py and llm.py.

    Returns True if names match, False on divergence.
    """
    ok = True

    seed_bb_names = {bb["name"] for bb in BUILDING_BLOCKS}
    llm_bb_names = set(LLM_BUILDING_BLOCKS.keys())
    if seed_bb_names != llm_bb_names:
        print("WARNING: BuildingBlock name mismatch!")
        print(f"  seed.py:  {sorted(seed_bb_names)}")
        print(f"  llm.py:   {sorted(llm_bb_names)}")
        print(f"  Only in seed: {sorted(seed_bb_names - llm_bb_names)}")
        print(f"  Only in llm:  {sorted(llm_bb_names - seed_bb_names)}")
        ok = False

    seed_gr_names = {gr["name"] for gr in GUARDRAILS}
    llm_gr_names = set(LLM_GUARDRAILS.keys())
    if seed_gr_names != llm_gr_names:
        print("WARNING: Guardrail name mismatch!")
        print(f"  seed.py:  {sorted(seed_gr_names)}")
        print(f"  llm.py:   {sorted(llm_gr_names)}")
        print(f"  Only in seed: {sorted(seed_gr_names - llm_gr_names)}")
        print(f"  Only in llm:  {sorted(llm_gr_names - seed_gr_names)}")
        ok = False

    if ok:
        print("Pre-check OK: BB/GR names match between seed.py and llm.py")
    return ok


def extract_sets_by_type(mappings, entity_type, threshold=0.0):
    """Extract a set of matched_name values for a given entity type above threshold."""
    return {
        m.matched_name
        for m in mappings
        if m.entity_type == entity_type and m.confidence >= threshold
    }


def compute_metrics(predicted: set, expected: set) -> dict:
    """Compute precision, recall, F1 for a single item."""
    tp = len(predicted & expected)
    fp = len(predicted - expected)
    fn = len(expected - predicted)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 1.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 1.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "predicted": sorted(predicted),
        "expected": sorted(expected),
    }


def main():
    print("=" * 60)
    print("BeeHaive Taxonomy Mapper Calibration")
    print("=" * 60)
    print()
    print("NOTE: This is a consistency check — it verifies that the")
    print("Gemini classifier reproduces the hand-curated labels from")
    print("seed.py (short summaries, 50-200 words). The 70% threshold")
    print("is a sanity check, not a production-precision guarantee.")
    print()

    # Pre-check taxonomy names
    if not pre_check_taxonomy():
        print("\nABORTED: Taxonomy names diverge. Fix before calibrating.")
        sys.exit(2)

    item_count = len(KNOWLEDGE_ITEMS)
    print(f"\nCalibrating {item_count} items...\n")

    # Accumulators per entity type, per threshold
    entity_types = ["BuildingBlock", "Guardrail", "Topic", "Author"]
    # {threshold: {entity_type: {"tp": 0, "fp": 0, "fn": 0}}}
    accum = {
        t: {et: {"tp": 0, "fp": 0, "fn": 0} for et in entity_types}
        for t in THRESHOLDS
    }

    per_item_results = []
    errors = []

    for i, item in enumerate(KNOWLEDGE_ITEMS, 1):
        title = item["title"]
        print(f"[{i}/{item_count}] {title}...")

        try:
            mappings = classify_text(
                text=item["content"],
                source_type=item["source_type"],
                title=title,
                confidence_threshold=0.0,  # Get all raw LLM output
            )
        except Exception as e:
            print(f"  ERROR: {e}")
            errors.append({"title": title, "error": str(e)})
            continue

        # Ground truth sets
        gt = {
            "BuildingBlock": set(item.get("building_blocks", [])),
            "Guardrail": set(item.get("guardrails", [])),
            "Topic": {t.lower() for t in item.get("topics", [])},
            "Author": {a.lower() for a in item.get("authors", [])},
        }

        item_result = {"title": title, "thresholds": {}}

        for threshold in THRESHOLDS:
            threshold_result = {}
            for et in entity_types:
                if et in ("Topic", "Author"):
                    predicted = {
                        m.matched_name.lower()
                        for m in mappings
                        if m.entity_type == et and m.confidence >= threshold
                    }
                else:
                    predicted = extract_sets_by_type(mappings, et, threshold)

                expected = gt[et]
                metrics = compute_metrics(predicted, expected)
                threshold_result[et] = metrics

                accum[threshold][et]["tp"] += metrics["tp"]
                accum[threshold][et]["fp"] += metrics["fp"]
                accum[threshold][et]["fn"] += metrics["fn"]

            item_result["thresholds"][str(threshold)] = threshold_result

        per_item_results.append(item_result)

        # Rate limiting
        if i < item_count:
            time.sleep(RATE_LIMIT_SECONDS)

    # Calculate aggregate metrics
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    aggregate_metrics = {}

    for threshold in THRESHOLDS:
        print(f"\n--- Threshold >= {threshold} ---")
        print(f"{'Entity Type':<16} {'Prec':>6} {'Recall':>6} {'F1':>6}  {'TP':>4} {'FP':>4} {'FN':>4}  {'Level':<12} {'Status'}")
        print("-" * 80)

        threshold_metrics = {}

        for et in entity_types:
            a = accum[threshold][et]
            tp, fp, fn = a["tp"], a["fp"], a["fn"]

            precision = tp / (tp + fp) if (tp + fp) > 0 else 1.0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 1.0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

            # Determine level and status
            if et in ("BuildingBlock", "Guardrail"):
                level = "normatief"
                status = "PASS" if precision >= EXIT_THRESHOLD else "FAIL"
            else:
                level = "informatief"
                status = "PASS" if precision >= EXIT_THRESHOLD else "WARN"

            print(f"{et:<16} {precision:>6.1%} {recall:>6.1%} {f1:>6.1%}  {tp:>4} {fp:>4} {fn:>4}  {level:<12} {status}")

            threshold_metrics[et] = {
                "level": level,
                "status": status,
                "precision": round(precision, 4),
                "recall": round(recall, 4),
                "f1": round(f1, 4),
                "tp": tp,
                "fp": fp,
                "fn": fn,
                "threshold": threshold,
            }

        aggregate_metrics[str(threshold)] = threshold_metrics

    # Interpretation help
    print("\n--- Interpretatie ---")
    print("- normatief: BuildingBlock/Guardrail (gesloten taxonomie, exacte match)")
    print("  → telt mee voor exitcode (precision >= 70% op threshold=0.7)")
    print("- informatief: Topic/Author (open taxonomie, case-insensitive match)")
    print("  → telt NIET mee voor exitcode, PASS/WARN ter indicatie")
    print("- Items met >= 3 guardrails: lagere recall (>=50%) is acceptabel")
    print("  gezien multi-label complexiteit.")

    if errors:
        print(f"\n--- Errors ({len(errors)}) ---")
        for err in errors:
            print(f"  {err['title']}: {err['error']}")

    # Determine exit code (BB + GR precision >= 70% at threshold=0.7)
    t07 = aggregate_metrics.get("0.7", {})
    bb_pass = t07.get("BuildingBlock", {}).get("precision", 0) >= EXIT_THRESHOLD
    gr_pass = t07.get("Guardrail", {}).get("precision", 0) >= EXIT_THRESHOLD

    print("\n--- Exit criteria (threshold=0.7) ---")
    print(f"BuildingBlock precision: {t07.get('BuildingBlock', {}).get('precision', 0):.1%} {'PASS' if bb_pass else 'FAIL'}")
    print(f"Guardrail precision:     {t07.get('Guardrail', {}).get('precision', 0):.1%} {'PASS' if gr_pass else 'FAIL'}")

    exit_ok = bb_pass and gr_pass
    print(f"\nOverall: {'PASS' if exit_ok else 'FAIL'}")

    # Save JSON results
    git_sha = get_git_sha()
    results = {
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "git_sha": git_sha,
        "item_count": item_count,
        "note": "Consistency check — ground truth is hand-curated seed.py, not independent validation.",
        "per_item_results": per_item_results,
        "aggregate_metrics": aggregate_metrics,
        "errors": errors,
    }

    output_path = Path(__file__).parent / "calibration-results.json"
    output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nResults saved to {output_path}")

    sys.exit(0 if exit_ok else 1)


if __name__ == "__main__":
    main()
