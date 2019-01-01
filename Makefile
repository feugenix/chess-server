.PHONY: all clean-pyc test coverage install run

install:
	pip install -r .meta/packages

run: install
	python -m server.app

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

test: install
	pytest

coverage: install
	coverage run -m pytest
	coverage report
