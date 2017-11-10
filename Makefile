bootstrap:
	@pip install -r requirements.txt

clean-pyc:
	@find . -name '*.pyc' -delete

clean-build:
	@rm -rf dist
	@rm -rf build
	@rm -rf *.egg-info

build-dist:
	@/usr/bin/env python setup.py sdist

build-release:
	@/usr/bin/env python setup.py bdist_wheel --universal

build-develop:
	@/usr/bin/env python setup.py develop

test:
	@/usr/bin/env python -m unittest discover

lint:
	@/usr/bin/env python -m flake8

clean: clean-pyc clean-build

dist: clean-build build-dist

release: clean-build build-release

develop: clean-build build-develop

check: lint test