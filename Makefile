ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

install:
	@poetry install --no-root --without test,dev

install-dev:
	@poetry  install --no-root

run:
	@poetry run python app/main.py

run-tests:
	@bash -c "LOCALPATH=${ROOT_DIR} poetry run python -m pytest"