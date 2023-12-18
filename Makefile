install:
	@poetry install --no-root --without test,dev

install-dev:
	@poetry  install --no-root

run:
	 @poetry run python app/main.py

run-tests:
	@poetry run python -m pytest