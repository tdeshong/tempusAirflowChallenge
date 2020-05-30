SHELL = /bin/bash
MODULE = dags

init:
	pip3 install -r requirements-setup.txt
	pip3 install -r requirements-test.txt
	pip3 install -r requirements.txt

run: clean
	@echo
	@echo --- Running Dockerized Airflow ---
	docker-compose -f docker/docker-compose.yml up --build

lint:
	@echo
	@echo --- Lint ---
	python3 -m flake8 ${MODULE}/

test:
	@echo
	@echo --- Test ---
	python3 -m pytest --cov=${MODULE} --cov-branch tests/

clean:
	@echo
	@echo --- Clean ---
	python3 setup.py clean
	find ${MODULE} | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	find tests | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	if [ -d ".pytest_cache" ]; then rm -r .pytest_cache; fi
	if [ -d ".coverage" ]; then rm  .coverage; fi

.PHONY: test
