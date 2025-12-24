# GENUIE ML Server

Production-ready FastAPI server for deploying TensorFlow ML models.

## Features
- Multi-model support (TensorFlow/Keras)
- REST API for predictions
- Docker containerized
- Model caching for performance
- Health checks and monitoring

## Quick Start

```bash
# Pull from Docker Hub
docker pull pradipk365/genuie-ml-server:latest

# Run the server
docker run -d -p 8000:8000 --name ml-server pradipk365/genuie-ml-server:latest

# Test
curl http://localhost:8000/
curl -X POST http://localhost:8000/predict/model_1 \\
  -H "Content-Type: application/json" \\
  -d '{"features": [1, 2, 3, 4, 5]}'
https://github.com/pdp-cloud/genuie-ml-server
https://hub.docker.com/r/pradipk365/genuie-ml-server
