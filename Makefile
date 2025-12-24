.PHONY: install VD-games build package-install lint lint-fix

install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uvx ruff check games_project_eremin/VD_games

lint-fix:
	uvx ruff check --fix games_project_eremin/VD_games