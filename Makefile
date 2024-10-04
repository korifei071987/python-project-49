#Makefile
# Poetry section
install: # inicializiation poetry-project
	poetry install
build: # distributive package-assembly
	poetry build
publish: # publication poetry-project (without add in PyPI)
	poetry publish --dry-run
package-install: # installing package from operating system (OS)
	python3 -m pip install --user dist/*.whl
# Game section
brain-games: # fast call brain-games
	poetry run brain-games
brain-even: # fast call game even/not even
	poetry run brain-even
brain-calc: # fast call game_calc
	poetry run brain-calc
brain-gcd: # fast call game_gcd
	poetry run brain-gcd
brain-progression: # fast call game_progression
	poetry run brain-progression
brain-prime: # fast call game_prime
	poetry run brain-prime
# Other
lint:
	poetry run flake8 brain_games
