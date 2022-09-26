.PHONY: virtualenv deps run test clean

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

clean:
	rm -rf __pycache__
	rm -rf ./.pytest_cache
#	rm -rf ${VENV}

test: init tests
	pytest --cache-clear
	make clean
