.PHONY: setup run graph-up graph-down graph-seed graph-reset test lint check fix ingest-item calibrate

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e "backend/[dev]"

run:
	.venv/bin/uvicorn app.main:app --app-dir backend --reload --port 8000

lint:
	.venv/bin/ruff check backend/

fix:
	.venv/bin/ruff check --fix backend/

test:
	.venv/bin/pytest -c backend/pyproject.toml --rootdir=backend -m integration -v

check: lint test

graph-up:
	docker compose up -d neo4j

graph-down:
	docker compose down

graph-seed:
	.venv/bin/python backend/scripts/seed_graph.py

graph-reset:
	docker compose exec neo4j cypher-shell -u neo4j -p "$${NEO4J_PASSWORD:-beehaive-dev}" "MATCH (n) DETACH DELETE n"
	$(MAKE) graph-seed

ingest-item:
	.venv/bin/python backend/scripts/ingest_item.py \
		--url "$(URL)" --title "$(TITLE)" --type "$(TYPE)" \
		$(if $(COMMIT),--commit,) $(if $(SKIP_RAG),--skip-rag,)

calibrate:
	.venv/bin/python backend/scripts/calibrate_mapper.py
