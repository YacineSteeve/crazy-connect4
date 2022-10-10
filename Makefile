.PHONY: virtualenv init run dev clean test

VENV = venv
PYTHON = ${VENV}/bin/python3
PIP = ${VENV}/bin/pip

virtualenv:
	python3 -m venv ${VENV}
	. ${VENV}/bin/activate

init: virtualenv requirements.txt
	${PIP} install -r requirements.txt

run: init main.py
	${PYTHON} main.py

dev: main.py
	clear; ${PYTHON} main.py

clean:
	rm -rf __pycache__
	rm -rf ./.pytest_cache
	rm -rf .coverage

test: tests src
	pytest --cov=src --cov-report=html --cache-clear --verbosity=1
	make clean
