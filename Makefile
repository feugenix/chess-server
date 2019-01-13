.PHONY: all clean-pyc test coverage install install-dev run

all: run

install:
	pip install -r .meta/packages_base

install-dev:
	pip install -r .meta/packages_dev

run: install
	python -m server.app

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

test: install-dev
	python -m unittest discover -s server

coverage: install-dev
	coverage run --source=server -m unittest discover
	coverage report
