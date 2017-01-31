.PHONY: install run

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
