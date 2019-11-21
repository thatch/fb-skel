PYTHON?=python
SOURCES=regen.py

.PHONY: venv
venv:
	$(PYTHON) -m venv .venv
	source .venv/bin/activate && make setup
	@echo 'run `source .venv/bin/activate` to use virtualenv'

# The rest of these are intended to be run within the venv, where python points
# to whatever was used to set up the venv.

.PHONY: setup
setup:
	python -m pip install -Ur requirements-dev.txt

.PHONY: format
format:
	python -m isort --recursive -y $(SOURCES)
	python -m black $(SOURCES)

.PHONY: lint
lint:
	python -m isort --recursive --diff $(SOURCES)
	python -m black --check $(SOURCES)
	python -m flake8 $(SOURCES)
	mypy --strict regen.py
