IMAGE_NAME := conradmugabe/issue-tracker-backend

build:
	docker build -t $(IMAGE_NAME) .

test-unit:
	docker run --rm -v $(PWD):/app $(IMAGE_NAME) pytest -svv --cov=src/ tests

lint:
	black src tests