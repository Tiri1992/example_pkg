.PHONY: help build dev test venv clean-cache clean-env clean-build clean-all

VENV_NAME?=env
VENV_ACTIVATE?=${VENV_NAME}/bin/activate
PYTHON:=${VENV_NAME}/bin/python3

help:
	@echo "make clean :: remove all builds, env, cached bin files."
	@echo "make clean-cache :: removes all cached binary files."
	@echo "make clean-env :: removes virtual environment."
	@echo "make clean-build :: removes build packages."
	@echo "make test :: runs all test suites."
	@echo "make dev :: prepares a development environment with required packages."
	@echo "make build-package :: packages the project by building both wheel and sdist in dist/."

$(VENV_ACTIVATE): setup.cfg pyproject.toml
	python -m venv $(VENV_NAME)
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -U build 
	$(PYTHON) -m pip install -e .[all]

dev: $(VENV_ACTIVATE)

test: $(VENV_ACTIVATE)
	$(PYTHON) -m pytest -v

clean-cache:
	rm -rf '.vscode'
	rm -rf **/*.eggs **/*.egg-info .cache .pytest_cache 
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

clean-env:
	rm -rf $(VENV_NAME)

clean-build:
	rm -rf './dist'
	rm -rf './build'

clean: clean-env clean-cache clean-build

build-package: $(PYTHON)
	$< -m build