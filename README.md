# Software Engineering Course Project

Description

## Usage

### Requirement

- Docker, docker compose

### Generate environment file for docker

```
docker compose run --rm gen-env
```

### Generate sample data for database

```
docker compose run --rm init-db
```

### Build tailwindcss

```
docker compose run --rm build-tailwindcss
```

### Start the project

```
docker compose up -d
```

## Development

### Environment

- Git
- EditorConfig
- Docker, Docker compose

### Start dev environment

```
docker compose -f docker-compose.dev.yml up -d
```

## Contribute

- Check and remove (or add to gitignore) cache files, temp files, ...

## Reference

### npm

- https://docs.npmjs.com/cli/v9/commands

### Tailwindcss

- https://tailwindcss.com/docs/installation

### jQuery

- https://releases.jquery.com/

### Docker

- https://hub.docker.com/_/nginx
- https://hub.docker.com/_/node
- https://hub.docker.com/_/mongo
- https://hub.docker.com/_/python

### Nginx

- https://www.nginx.com/resources/wiki/start/topics/examples/full/
- https://nginx.org/en/docs/

### MongoDB

- https://www.mongodb.com/docs/manual/reference/program/mongod/
- https://www.mongodb.com/docs/manual/reference/configuration-options/
- https://www.mongodb.com/docs/manual/reference/connection-string/

### Python

- https://pymongo.readthedocs.io/en/stable/tutorial.html
- https://argon2-cffi.readthedocs.io/en/stable/api.html
- https://jwt.io/libraries?language=Python
- https://github.com/lepture/authlib
