init:		poetry install

run:		poetry run agentflow start
test:		poetry run pytest tests/ --cov=agentflow
doc:		poetry run mkdocs build
bench:		POETRY_VIRTUAL_ENVS_CREATE=true poetry run locust -f tests/perf/test_bench.py
lint:		poetry run mypy agentflow
		poetry run pycodestyle agentflow
install:		pip install -e .
dev:		python -m venv .venv && . .venv/bin/activate && pip install -r requirements.dev.txt
