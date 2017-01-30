.PHONY: run

# Initialization ===============================================================

install:

# Run ===============================================================

#docker run -it --rm --name awale -v "$PWD":/home/max/app/awale -w /home/max/app/awale python:3 python src/launcher.py

run:
	docker run -it --rm \
		-v "$(PWD)":/home/max/app/awale \
		-w /home/max/app/awale \
		python:3 \
	 	python src/launcher.py
