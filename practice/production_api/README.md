# Production-Ready REST API

A production-grade REST API built with FastAPI, featuring authentication, database management, comprehensive logging, and deployment configurations.

## 🚀 Features

- **FastAPI Framework** - Modern, fast, and async-first web framework
- **JWT Authentication** - Secure user authentication with access and refresh tokens
- **PostgreSQL Database** - Production-ready relational database with async support
- **SQLAlchemy ORM** - Database models and migrations with Alembic
- **Pydantic Validation** - Request/response validation and serialization
- **Structured Logging** - JSON-formatted logs with request tracking
- **Error Handling** - Comprehensive exception handling with custom middleware
- **API Documentation** - Auto-generated OpenAPI (Swagger) docs
- **Testing Suite** - Unit and integration tests with pytest
- **Docker Support** - Multi-container setup with Docker Compose
- **Nginx Reverse Proxy** - Production-ready web server with rate limiting
- **Monitoring** - Prometheus metrics endpoint
- **Security** - CORS, security headers, password hashing with bcrypt

## 📁 Project Structure

```
production_api/
├── app/
│   ├── api/                 # API endpoints
│   │   ├── auth.py         # Authentication routes
│   │   ├── users.py        # User management routes
│   │   ├── jokes.py        # Joke endpoints
│   │   └── health.py       # Health check
│   ├── core/               # Core functionality
│   │   ├── config.py       # Configuration management
│   │   ├── security.py     # Authentication utilities
│   │   └── logging.py      # Logging configuration
│   ├── db/                 # Database
│   │   └── session.py      # Database session management
│   ├── models/             # SQLAlchemy models
│   │   ├── user.py
│   │   └── joke.py
│   ├── schemas/            # Pydantic schemas
│   │   ├── user.py
│   │   ├── joke.py
│   │   └── common.py
│   ├── services/           # Business logic
│   │   ├── user_service.py
│   │   └── joke_service.py
│   ├── middleware.py       # Custom middleware
│   ├── exceptions.py       # Exception handlers
│   └── main.py            # Application entry point
├── tests/                  # Test suite
├── alembic/               # Database migrations
├── Dockerfile             # Container definition
├── docker-compose.yml     # Multi-container orchestration
├── nginx.conf            # Nginx configuration
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md           # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Redis (optional, for caching)
- Docker & Docker Compose (for containerized deployment)

### Local Development Setup

1. **Clone the repository**
   ```bash
   cd production_api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Set up database**
   ```bash
   # Create PostgreSQL database
   createdb production_db
   
   # Run migrations
   alembic upgrade head
   ```

6. **Run the application**
   ```bash
   python -m app.main
   # Or with uvicorn directly
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

7. **Access the API**
   - API: http://localhost:8000
   - Swagger Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 🐳 Docker Deployment

### Quick Start with Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop all services
docker-compose down
```

### Services

- **API**: http://localhost:8000
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379
- **Nginx**: http://localhost:80

### Build and Run Manually

```bash
# Build image
docker build -t production-api .

# Run container
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql+asyncpg://user:pass@host/db \
  production-api
```

## 🔑 API Endpoints

### Authentication

- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get tokens
- `POST /auth/refresh` - Refresh access token

### Users

- `GET /users/me` - Get current user
- `GET /users/{user_id}` - Get user by ID
- `GET /users/` - List users (paginated)
- `PUT /users/me` - Update current user
- `DELETE /users/me` - Delete current user

### Jokes

- `GET /jokes/random` - Get random joke
- `GET /jokes/` - List cached jokes
- `GET /jokes/{joke_id}` - Get joke by ID

### System

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /metrics` - Prometheus metrics

## 🔒 Authentication

The API uses JWT (JSON Web Tokens) for authentication:

1. **Register**: Create a new account
   ```bash
   curl -X POST http://localhost:8000/auth/register \
     -H "Content-Type: application/json" \
     -d '{
       "email": "user@example.com",
       "username": "myuser",
       "password": "securepass123",
       "full_name": "John Doe"
     }'
   ```

2. **Login**: Get access token
   ```bash
   curl -X POST http://localhost:8000/auth/login \
     -H "Content-Type: application/json" \
     -d '{
       "username": "myuser",
       "password": "securepass123"
     }'
   ```

3. **Use Token**: Include in Authorization header
   ```bash
   curl http://localhost:8000/users/me \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
   ```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_auth.py

# Run with verbose output
pytest -v
```

## 📊 Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Rollback one version
alembic downgrade -1

# Show migration history
alembic history
```

## 📝 Environment Variables

Key environment variables (see `.env.example` for full list):

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `SECRET_KEY` | JWT secret key | Required |
| `ENVIRONMENT` | Environment (dev/staging/prod) | production |
| `DEBUG` | Debug mode | False |
| `LOG_LEVEL` | Logging level | INFO |
| `ALLOWED_ORIGINS` | CORS allowed origins | localhost:3000 |

## 🚦 Production Deployment

### Prerequisites

1. PostgreSQL database
2. Redis server (optional)
3. Domain name with SSL certificate

### Deployment Steps

1. **Configure environment**
   ```bash
   # Set production environment variables
   export DATABASE_URL="postgresql+asyncpg://..."
   export SECRET_KEY="your-secure-secret-key"
   export ENVIRONMENT="production"
   ```

2. **Run migrations**
   ```bash
   alembic upgrade head
   ```

3. **Start with Docker Compose**
   ```bash
   docker-compose -f docker-compose.yml up -d
   ```

4. **Configure Nginx/SSL**
   - Update `nginx.conf` with your domain
   - Add SSL certificates
   - Enable HTTPS configuration

### Performance Tuning

- Adjust `WORKERS` based on CPU cores (2 * cores + 1)
- Configure database connection pool size
- Enable Redis for caching
- Set up CDN for static assets
- Configure rate limiting

## 📈 Monitoring

### Prometheus Metrics

Access metrics at `/metrics`:
```bash
curl http://localhost:8000/metrics
```

### Logs

Structured JSON logs are written to stdout:
```bash
# View logs in Docker
docker-compose logs -f api

# Filter by log level
docker-compose logs api | grep ERROR
```

### Health Check

```bash
curl http://localhost:8000/health
```

## 🔧 Development

### Code Quality

```bash
# Format code
black app/ tests/

# Sort imports
isort app/ tests/

# Type checking
mypy app/

# Linting
flake8 app/
```

### Adding New Endpoints

1. Create route in `app/api/`
2. Define schema in `app/schemas/`
3. Implement service in `app/services/`
4. Add tests in `tests/`

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License.

## 📧 Support

For issues and questions, please open an issue on GitHub.

## 🎯 Roadmap

- [ ] Rate limiting with Redis
- [ ] Email verification
- [ ] OAuth2 integration
- [ ] WebSocket support
- [ ] Background tasks with Celery
- [ ] API versioning
- [ ] GraphQL endpoint
- [ ] Admin dashboard

## 🙏 Acknowledgments

- FastAPI - https://fastapi.tiangolo.com/
- SQLAlchemy - https://www.sqlalchemy.org/
- Pydantic - https://pydantic-docs.helpmanual.io/
