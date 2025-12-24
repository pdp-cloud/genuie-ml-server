#!/bin/bash
echo "========================================="
echo "GENUIE ML Server - Complete API Test"
echo "========================================="
echo ""

echo "1. Checking if server is running..."
docker ps | grep ml-server
if [ $? -eq 0 ]; then
    echo "✅ Server is running"
else
    echo "❌ Server is not running"
    echo "Starting server..."
    docker run -d -p 8000:8000 --name ml-server pradipk365/genuie-ml-server:latest
    sleep 5
fi

echo ""
echo "2. Testing API Endpoints:"
echo "-------------------------"

echo "a) Health Check (/):"
curl -s http://localhost:8000/ | python3 -c "import sys, json; print(json.dumps(json.load(sys.stdin), indent=2))"
echo ""

echo "b) List Models (/models):"
curl -s http://localhost:8000/models | python3 -c "import sys, json; print(json.dumps(json.load(sys.stdin), indent=2))"
echo ""

echo "c) Make Prediction (/predict/model_1):"
curl -s -X POST http://localhost:8000/predict/model_1 \
  -H "Content-Type: application/json" \
  -d '{"features": [10, 20, 30, 40, 50]}' \
  | python3 -c "import sys, json; print(json.dumps(json.load(sys.stdin), indent=2))"
echo ""

echo "d) Another Prediction:"
curl -s -X POST http://localhost:8000/predict/model_1 \
  -H "Content-Type: application/json" \
  -d '{"features": [1.1, 2.2, 3.3, 4.4, 5.5]}' \
  | python3 -c "import sys, json; print(json.dumps(json.load(sys.stdin), indent=2))"
echo ""

echo "========================================="
echo "✅ API Test Complete!"
echo "Server URL: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"
echo "========================================="
