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
brain-games: # fast call game 
	poetry run brain-games 
