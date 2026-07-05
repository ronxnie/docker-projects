# DockerImage_Network_Training

A simple Flask-based microservice demo with separate frontend and backend services.

- `backend/` provides a health endpoint and an API endpoint returning a backend message.
- `frontend/` calls the backend service and returns a combined response.

## Project structure

- `backend/app.py` - Flask backend service.
- `backend/requirements.txt` - backend Python dependencies.
- `backend/Dockerfile` - backend container build file (currently empty).
- `frontend/app.py` - Flask frontend service.
- `frontend/requirements.txt` - frontend Python dependencies.
- `frontend/Dockerfile` - frontend container build file for a Python 3.9 runtime.

## Requirements

- Python 3.11+ is recommended
- `pip` for installing Python dependencies

## Local setup

> If you are using WSL, run these commands in your WSL shell from the project root directory.

### Backend

1. Change into the backend directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend service:
   ```bash
   python app.py
   ```
4. The backend listens on port `5000` by default.

### Frontend

1. Change into the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the frontend service:
   ```bash
   python app.py
   ```
4. The frontend listens on port `8080` by default.

## Service endpoints

### Backend

- `GET /health` — returns backend health status.
- `GET /api/message` — returns a JSON payload from the backend.

### Frontend

- `GET /health` — returns frontend health status.
- `GET /` — forwards a request to the backend and returns the combined response.

## Configuration

- `BACKEND_URL` environment variable controls which backend URL the frontend uses.
- `PORT` environment variable can override the listening port for each service.

Example frontend configuration:
```bash
export BACKEND_URL=http://localhost:5000
export PORT=8080
python app.py
```

## Docker build and run

### Backend container

From `backend/`:
```bash
docker build -t flask-app-backend:v1.0 ./backend
docker run -d --name backend -p 5000:5000 flask-app-backend:v1.0
```

In WSL from the project root:
```bash
docker build -t flask-app-backend:v1.0 ./backend
docker run -d --name backend -p 5000:5000 flask-app-backend:v1.0
```

### Frontend container

From `frontend/`:
```bash
docker build -t flask-app-frontend:v1.0 ./frontend
docker run -d --name frontend -p 8080:8080 flask-app-frontend:v1.0
```

In WSL from the project root:
```bash
docker build -t flask-app-frontend:v1.0 ./frontend
docker run -d --name frontend -p 8080:8080 flask-app-frontend:v1.0
```

After running containers, verify them with:
```bash
docker ps -a
```

Inspect the Docker bridge network details with:
```bash
docker network inspect bridge
```

Create a new bridge network:
```bash
docker network create appnet
```

Stop the containers:
```bash
docker stop backend frontend
```

Remove the stopped containers:
```bash
docker rm backend frontend
```

Remove the built images:
```bash
docker rmi flask-app-backend:v1.0 flask-app-frontend:v1.0
```

Run the docker images on the custom created bridge appnet:
```bash
docker run -d --name backend --network appnet -p 5000:5000 flask-app-backend:v1.0
docker run -d --name frontend --network appnet -p 8080:8080 flask-app-frontend:v1.0
```

> In WSL, `host.docker.internal` is commonly available to access services running on the Windows host from containers.

## Notes

- The frontend currently expects the backend service to be reachable at `http://backend:5000` by default.
- Both Dockerfiles use `python:3.9-slim`, install dependencies from `requirements.txt`, copy the app files, expose the service port, and run `python app.py`.

## Troubleshooting

- If the frontend returns `backend unreachable`, verify the backend is running and reachable at the configured `BACKEND_URL`.
- Use `curl` or a browser to access `/health` endpoints for basic validation.
