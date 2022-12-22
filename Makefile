install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

check: build publish package-install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

gendiff:
	poetry run gendiff
