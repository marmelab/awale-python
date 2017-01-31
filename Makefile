.PHONY: install run test lint

BIN := docker run \
			-it \
			--rm \
			awale-python

# Initialization ===============================================================

install:
	docker build --tag=awale-python .

# Run ===============================================================

run:
	$(BIN) python src/launcher.py

# Tests ===============================================================

test:
	$(BIN) python -m unittest discover

# Lint ===============================================================

lint:
	$(BIN) pep8 . --max-line-length=150
