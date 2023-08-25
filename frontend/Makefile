PROJECT_NAME=frontend
DEV_IMAGE_NAME=$(PROJECT_NAME)-dev
DEV_CONTAINER_NAME=$(PROJECT_NAME)-dev-container

.PHONY: build, run, stop

build:
	docker build -t $(DEV_IMAGE_NAME) -f Dockerfile.dev .

run:
	docker run --rm --name $(DEV_CONTAINER_NAME) -p 3000:3000 -v $(shell pwd)/src/:/app/src/ -v $(shell pwd)/public/:/app/public/ -v $(shell pwd)/.env:/app/.env $(DEV_IMAGE_NAME)

stop:
	docker stop $(DEV_CONTAINER_NAME)
