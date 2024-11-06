# <div style="text-align:center;color:green;">Docker Commands </div>

#### To build a Docker image from a `Dockerfile`:

```bash
docker build -t <image-name>:<tag> .
```

- <image-name>: The name you want to give to your Docker image.
- \<tag>: The version tag (e.g., latest, v1).

#### Example:

```bash
docker build -t my-app:latest .
```

### List Docker Images

#### To list all available Docker images on your system:

```bash
docker images
```

### Run Docker Container

#### To run a container from an image:

```bash
docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>:<tag>
```

- <host-port>: Port on your host machine.
- <container-port>: Port inside the container.
- <container-name>: The name for your running container.
- <image-name>:<tag>: Image name and tag (e.g., my-app:latest).

#### Example:

```bash
docker run -d -p 5000:5000 --name my-running-app my-app:latest
```

### View Running Containers

#### To see the list of running Docker containers:

```bash
docker ps
```

### Stop Docker Container

#### To stop a running container:

```bash
docker stop <container-name>
```

#### Example:

```bash

docker stop my-running-app
```

### Remove Docker Container

#### To remove a stopped container:

```bash
docker rm <container-name>
```

#### Example:

```bash

docker rm my-running-app
```

### Remove Docker Image

#### To remove a Docker image:

```bash
docker rmi <image-name>:<tag>
```

#### Example:

```bash
docker rmi my-app:latest
```

### View Docker Logs

#### To view logs for a container:

```bash
docker logs <container-name>
```

#### Example:

```bash
docker logs my-running-app
```

## Docker Compose Commands

### Start Services

#### To start services defined in docker-compose.yml:

```bash
docker-compose up
```

#### To start services in detached mode:

```bash
docker-compose up -d
```

#### Stop Services

### To stop services:

```bash
docker-compose down
```

### View Logs

#### To view logs for all services:

```bash
docker-compose logs
```

### Build Docker Images with Docker Compose

#### To build the images defined in docker-compose.yml:

```bash
docker-compose build
```
