.PHONY: all clean-pyc test coverage install

install:
	pip install

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

test: install
	pytest

coverage: install
	coverage run -m pytest
	coverage report
