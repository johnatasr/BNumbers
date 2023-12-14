.PHONY: build_docker run_docker tests lint run

IMAGE_NAME := bnumbers
TAG := latest

build_docker:
	docker build -t $(IMAGE_NAME):$(TAG) .

run_docker:
	docker run -it $(IMAGE_NAME):$(TAG)

tests:
	pytest

lint:
	flake8 app
	isort app
	black app

run:
	@python main.py