SHELL := /bin/bash
.ONESHELL:
.DEFAULT_GOAL := help

PYTHON := uv run python
PYTEST := uv run -m pytest

.PHONY: help new test

help: ## Show available targets
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z0-9_.-]+:.*##/ {printf "\033[36m%-14s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

new: ## Run new.py (pass args: make run ARGS="--foo bar")
	$(PYTHON) new.py $(ARGS)

test: ## Run pytest
	$(PYTEST) $(ARGS)

