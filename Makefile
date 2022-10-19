.PHONY: clean test

clean:
	rm -rf __pycache__
	rm -rf ./.pytest_cache
	rm -rf ./htmlcov/
	rm .coverage

test: tests src
	pytest --cov=src --cov-report=html --cache-clear --verbosity=1
	make clean
