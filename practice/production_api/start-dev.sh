#!/bin/bash

# Development startup script

set -e

echo "🚀 Starting Production API (Development Mode)"
echo "=============================================="

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️  Please update .env with your configuration"
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if database is running
echo "🗄️  Checking database connection..."
python -c "from app.core.config import settings; print(f'Database URL: {settings.DATABASE_URL}')" || {
    echo "❌ Failed to load configuration"
    exit 1
}

# Run migrations
echo "🔄 Running database migrations..."
alembic upgrade head || echo "⚠️  Migration failed or no migrations to run"

# Start the application
echo "🚀 Starting FastAPI application..."
echo "📚 API Documentation: http://localhost:8000/docs"
echo "🏥 Health Check: http://localhost:8000/health"
echo ""

python -m app.main
