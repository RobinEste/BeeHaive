.PHONY: setup graph-up graph-down graph-seed graph-reset test lint check fix

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e "backend/[dev]"

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
