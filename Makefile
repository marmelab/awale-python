.PHONY: install run test lint

BIN := docker run \
    -it \
    --rm \
    -v "$(PWD):/app" \
    awale-python

# Initialization ===============================================================

install:
	docker build --tag=awale-python .

# Run ===============================================================

run:
	$(BIN) python3 /app/src/launcher.py

# Tests ===============================================================

test:
	$(BIN) python3 -m unittest discover --v

# Lint ===============================================================

lint:
	$(BIN) pep8 .
