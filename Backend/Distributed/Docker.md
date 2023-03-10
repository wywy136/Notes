# Docker

Run a container from an image

```shell
docker run hello-world
```

List images

```shell
docker image
```

## Dockerfile

- ADD: `ADD <file> <path>`

Build a docker image from a Dockerfile

```shell
docker build -t <tag>
```

Run a docker container with flag

https://docs.docker.com/engine/reference/run/

```
docker run <tag>
```

- -d (--detach) run container in background
- -i (--interactive) Keep STDIN open
- --rm remove the container when its finished
- -v map a volume
- -p (--publish) publish container ports to the host (for networking)
- --name name for the container

Mount a local file path

```sh
docker run -v <absolute_local_path>:<path_in_container> -it <container_tag> /bin/bash
```

## Docker file, Docker image and Docker container

- Dockerfile is a text file that Docker will read and analyze it and produce a Docker image, in other words, it's a recipe.
- Docker image is a read-only template that contains a set of instructions for creating a container that can run on the Docker platform.
- When we run a docker image, then we will create a container, which is an isolated sandbox environment where we could do the operations
