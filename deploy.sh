#!/bin/bash
echo "Deploying GENUIE ML Server..."
echo ""

# Stop existing container
echo "1. Stopping existing container..."
docker stop ml-server 2>/dev/null || true
docker rm ml-server 2>/dev/null || true

# Pull latest image
echo "2. Pulling latest image from Docker Hub..."
docker pull pradipk365/genuie-ml-server:latest

# Run new container
echo "3. Starting new container..."
docker run -d \
  -p 8000:8000 \
  --name ml-server \
  --restart unless-stopped \
  pradipk365/genuie-ml-server:latest

# Wait for startup
echo "4. Waiting for server to start..."
sleep 5

# Test
echo "5. Testing deployment..."
curl -s http://localhost:8000/ > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Deployment successful!"
    echo "   Server: http://localhost:8000"
    echo "   API Docs: http://localhost:8000/docs"
else
    echo "❌ Deployment failed"
    docker logs ml-server
fi
