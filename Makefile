SHELL := /bin/bash
.ONESHELL:
.DEFAULT_GOAL := help

PYTEST := uv run -m pytest

.PHONY: help test

help: ## Show available targets
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z0-9_.-]+:.*##/ {printf "\033[36m%-14s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

test: ## Run pytest
	$(PYTEST) $(ARGS)

