.DEFAULT_GOAL := help

PROJ := chcode
PROJ_ROOT := src/$(PROJ)

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-10s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: clean
clean: ## remove build artifacts
	rm -rf build/ \
	       docs/ \
	       dist/ \
	       .eggs/
	find . -name '.eggs' -type d -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: dist
dist: clean ## builds source and wheel package
	python setup.py sdist bdist_wheel

.PHONY: release
release: dist ## package and upload a release
	twine upload dist/*

.PHONY: lint
lint: ## check style with pylint
	pylint $(PROJ_ROOT)
	mypy $(PROJ_ROOT)/
	pytype -j auto $(PROJ_ROOT)/

.PHONY: test
test: ## run test suite
	pytest --cov=$(PROJ) $(PROJ_ROOT)

.PHONY: install
install: ## install the package with dev dependencies
	pip install -e . -r requirements_dev.txt

.PHONY: sync
sync: ## completely sync installed packages with dev dependencies
	pip-sync requirements_dev.txt
	pip install -e .

.PHONY: lock
lock: ## lock versions of third-party dependencies
	pip-compile-multi --directory . \
		--allow-unsafe \
		-t requirements_dev.in \
		--use-cache \
		--no-upgrade

.PHONY: upgrade
upgrade: ## upgrade versions of third-party dependencies
	pip-compile-multi --directory . \
		--allow-unsafe \
		-t requirements_dev.in \
		--use-cache
