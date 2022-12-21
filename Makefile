setup: install lint build publish package-install

install:
	poetry install

lint:
	poetry run flake8 gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

gendiff:
	poetry run gendiff
