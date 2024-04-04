.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")

.PHONY: help
help:			## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: venv
venv:			## Create a virtual environment
	@echo "Creating virtualenv ..."
	@rm -rf .venv
	@python3 -m venv .venv
	@./.venv/bin/pip install -U pip
	@echo
	@echo "Run 'source .venv/bin/activate' to enable the environment"

.PHONY: install
install:		## Install dependencies
	pip install -r requirements-dev.txt

.PHONY: api-test
test:		## Run api-tests and coverage
	mkdir -p reports/coverage || true
	pytest --cov=src tests

SERVER_URL = 0.0.0.0:8000
.PHONY: run-server
run-server: 		## Run the server
	gunicorn --bind $(SERVER_URL) src.main:app --reload -k uvicorn.workers.UvicornWorker
