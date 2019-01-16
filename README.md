# python-app-with-docker

Example. There is dockerfile with simple python-web service.

Run docker container and extract result from it.

## Running in Docker containers

### Using docker:
To run application you should run commands:
 1. ```docker build --tag={CONTAINER_NAME} --no-cache .```
 2. ```docker run {CONTAINER_NAME}```
 
 This 2 commands will rebuilds container and starts application.
 
### Using docker-compose:
Command ```docker-compose -f docker-compose.yml up``` will create and deploy application (service) 
defined in docker-compose.yml file.
