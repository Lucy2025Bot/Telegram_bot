#!/bin/bash
echo "Starting Bot Deployment..."
pip install -r requirements.txt
uvicorn bot:app --host 0.0.0.0 --port 10000
