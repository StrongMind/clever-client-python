
.PHONY: test

test:
	python -m unittest

install: test-requirements.txt requirements.txt
	pip install -r test-requirements.txt
	pip install -r requirements.txt

build:
	python setup.py sdist
