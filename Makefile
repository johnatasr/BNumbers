.PHONY: build_docker, run_docker, tests, run

build_docker:
    docker build

run_docker:
    docker run

tests:
    pytest

lint:
    black app
    isort app

run:
    @python main.py

