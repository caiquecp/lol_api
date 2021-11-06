format:
	black -l 120 lol_api

check-typing:
	mypy lol_api

run:
	python -m lol_api