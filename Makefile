install:
	poetry install
	
start-game:
    poetry run start-game
    
build:
    poetry build
	
publish:
    poetry publish --dry-run

package-install:
    python3 -m pip install --user --force-reinstall dist/*.whl
	
make lint:
	poetry run flake8 lotto-game
	
run_test:
	poetry run pytest --cov=lotto_game tests/ --cov-report xml