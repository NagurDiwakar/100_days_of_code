#!/bin/bash

# Production API Deployment Script
# This script helps deploy the application to production

set -e

echo "🚀 Production API Deployment Script"
echo "===================================="

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root or with sudo"
    exit 1
fi

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo "❌ .env file not found. Please create it from .env.example"
    exit 1
fi

# Check required environment variables
required_vars=("DATABASE_URL" "SECRET_KEY")
for var in "${required_vars[@]}"; do
    if [ -z "${!var}" ]; then
        echo "❌ Required environment variable $var is not set"
        exit 1
    fi
done

echo "✅ Environment variables validated"

# Pull latest code
echo "📥 Pulling latest code..."
git pull origin main

# Build Docker images
echo "🏗️  Building Docker images..."
docker-compose build

# Run database migrations
echo "🗄️  Running database migrations..."
docker-compose run --rm api alembic upgrade head

# Stop old containers
echo "🛑 Stopping old containers..."
docker-compose down

# Start new containers
echo "🚀 Starting new containers..."
docker-compose up -d

# Wait for services to be healthy
echo "⏳ Waiting for services to be healthy..."
sleep 10

# Check health
echo "🏥 Checking application health..."
health_response=$(curl -s http://localhost:8000/health || echo "failed")

if [[ $health_response == *"healthy"* ]]; then
    echo "✅ Deployment successful! Application is healthy."
else
    echo "❌ Deployment may have issues. Health check failed."
    docker-compose logs --tail=50 api
    exit 1
fi

# Show running containers
echo ""
echo "📦 Running containers:"
docker-compose ps

echo ""
echo "✅ Deployment completed successfully!"
echo "🌐 API is available at: http://$(hostname -I | awk '{print $1}'):8000"
echo "📚 API docs: http://$(hostname -I | awk '{print $1}'):8000/docs"
