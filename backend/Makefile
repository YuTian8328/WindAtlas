xx	PROJECT_NAME=backend
DEV_IMAGE_NAME=$(PROJECT_NAME)-dev
DEV_CONTAINER_NAME=$(PROJECT_NAME)-dev-container
PROD_IMAGE_NAME=$(PROJECT_NAME)
PROD_CONTAINER_NAME=$(PROJECT_NAME)-container

.PHONY: dev-build, dev-run, dev-stop, prod-build, prod-run, prod-stop

dev-build:
	docker build -t $(DEV_IMAGE_NAME) -f Dockerfile.dev .

dev-run:
	docker run --rm --name $(DEV_CONTAINER_NAME) -p 8000:8000 -v $(shell pwd):/app $(DEV_IMAGE_NAME)

dev-stop:
	docker stop $(DEV_CONTAINER_NAME)

prod-build:
	docker build -t $(PROD_IMAGE_NAME) .

prod-run:
	docker run --rm --name $(PROD_CONTAINER_NAME) -p 8000:8000 $(PROD_IMAGE_NAME)

prod-stop:
	docker stop $(PROD_CONTAINER_NAME)
