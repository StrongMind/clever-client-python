
.PHONY: test

test:
	python -m unittest

install: requirements-dev.txt requirements.txt
	pip install -r requirements-dev.txt
	pip install -r requirements.txt
