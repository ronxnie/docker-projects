# Dockerized Flask Microservices

This project contains two simple Flask applications that run as separate microservices using Docker and Docker Compose.

## Project Structure

```text
DockerApplication/
├── Microservice1/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── Microservice2/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## What This Project Does

- Microservice 1 exposes a simple Flask app at the root URL.
- Microservice 2 exposes another simple Flask app at the root URL.
- Both services are containerized using Docker.
- Docker Compose is used to build and run both services together.

## Prerequisites

Make sure the following are installed on your machine:

- Docker
- Docker Compose

You can verify installation with:

```bash
docker --version
docker compose version
```

## How to Run the Project

### 1. Clone or open the project folder

Navigate to the project directory:

```bash
cd DockerApplication
```

### 2. Build and start the containers

Run:

```bash
docker compose up --build
```

This will:
- Build the Docker image for Microservice 1
- Build the Docker image for Microservice 2
- Start both containers

### 3. Access the applications

Once the containers are running, open the following URLs in your browser:

- Microservice 1: http://localhost:5001
- Microservice 2: http://localhost:5002

## Stopping the Project

To stop and remove the containers:

```bash
docker compose down
```

## Rebuilding After Changes

If you change the app code or Dockerfiles, rebuild the containers with:

```bash
docker compose up --build
```

## Service Details

### Microservice 1
- Folder: Microservice1
- Port inside container: 5000
- Port exposed on host: 5001

### Microservice 2
- Folder: Microservice2
- Port inside container: 5000
- Port exposed on host: 5002

## Notes

- The Flask apps are intentionally simple for learning and demonstration purposes.
- You can modify the route responses in the app.py files to customize behavior.

## Troubleshooting

If the containers fail to start:

1. Check Docker is running.
2. Rebuild the containers.
3. Review container logs with:

```bash
docker compose logs
```
