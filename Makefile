# Define variables
DOCKER_COMPOSE = docker-compose
DOCKER_COMPOSE_FILE = docker-compose.yml

# Define targets
.PHONY: build up down clean

build:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) build

up:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up

down:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down

clean:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down -v --remove-orphans
