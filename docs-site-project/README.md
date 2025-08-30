# Documentation Site

A modern, responsive documentation platform built with Flask, featuring live markdown editing, search functionality, and Docker deployment.

## ✨ Features

- 📝 **Live Markdown Editor** - Write and preview documentation in real-time
- 🔍 **Full-text Search** - Find content across all documents
- 🐳 **Docker Support** - Easy containerized deployment
- 📱 **Responsive Design** - Works perfectly on all devices
- 🚀 **Auto-deployment** - Automated build and deploy scripts
- 💾 **Auto-save** - Never lose your work
- 🎨 **Modern UI** - Clean, professional interface
- 📊 **API Access** - RESTful API for programmatic access

## 🚀 Quick Start

### Option 1: Quick Setup
```bash
python setup.py
python app.py
```

### Option 2: Full Setup with Deployment Manager
```bash
python deploy.py --setup
python deploy.py --dev
```

### Option 3: Docker
```bash
python deploy.py --docker
```

Then open http://localhost:5000 in your browser.

## 📁 Project Structure

```
docs-site-project/
├── app.py                 # Main Flask application
├── deploy.py             # Deployment automation script
├── setup.py              # Quick setup script
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose setup
├── site_config.yaml     # Site configuration
├── templates/           # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── document.html
│   ├── editor.html
│   └── search.html
├── docs/               # Documentation files (markdown)
└── static/            # Static assets (CSS, JS, images)
```

## 🛠️ Commands

### Development
```bash
# Setup environment
python deploy.py --setup

# Run development server
python deploy.py --dev

# Run tests
python deploy.py --test
```

### Docker Deployment
```bash
# Build Docker image
python deploy.py --build

# Run Docker container
python deploy.py --docker

# Deploy with Docker Compose (includes Nginx)
python deploy.py --compose

# Full deployment (setup + build + deploy)
python deploy.py --all
```

### GitHub Actions Automation
```bash
# Validate GitHub Actions workflows
python github_actions_helper.py --validate

# Test Docker build locally
python github_actions_helper.py --test-docker

# Simulate GitHub Actions locally
python github_actions_helper.py --simulate

# Run all GitHub Actions checks
python github_actions_helper.py --all
```

### Management
```bash
# Check deployment status
python deploy.py --status

# Stop all services
python deploy.py --stop

# Generate deployment guide
python github_actions_helper.py --generate-guide
```

## 📝 Writing Documentation

1. **Create New Document**: Click "New Document" or go to `/new`
2. **Edit Existing**: Click "Edit" on any document
3. **Markdown Support**: Full markdown syntax with syntax highlighting
4. **Live Preview**: See changes in real-time as you type
5. **Auto-save**: Use Ctrl+S or Cmd+S to save

### Markdown Features Supported
- Headers (H1-H6)
- **Bold** and *italic* text
- `Inline code` and code blocks
- Lists (numbered and bulleted)
- Links and images
- Tables
- Task lists
- Syntax highlighting for code

## 🔍 Search

Use the search box in the navigation to find content across all documents. The search is full-text and case-insensitive.

## 🌐 API Endpoints

- `GET /` - Homepage with document list
- `GET /doc/<filename>` - View document
- `GET /edit/<filename>` - Edit document
- `POST /save` - Save document
- `GET /api/docs` - JSON list of all documents
- `GET /search?q=query` - Search documents

## 🐳 Docker

### Build and Run
```bash
docker build -t docs-site .
docker run -p 5000:5000 -v $(pwd)/docs:/app/docs docs-site
```

### Using Docker Compose
```bash
docker-compose up -d
```

This will start:
- Documentation site on port 5000
- Nginx reverse proxy on port 80

## ⚙️ Configuration

Edit `site_config.yaml` to customize:

```yaml
site_name: "Your Documentation Site"
description: "Your site description"
version: "1.0.0"
author: "Your Name"

docker:
  image_name: "your-docs-site"
  container_name: "your-docs-app"
  port: 5000
```

## 🚀 Deployment Options

### Local Development (Already Running!)
Your site is running at http://localhost:5000

### GitHub Actions (Automated CI/CD)
- **Automatic deployment** on push to main branch
- **Multi-platform support** (Heroku, AWS, Digital Ocean, etc.)
- **Docker builds** with security scanning
- **Automated testing** and quality checks

**Setup GitHub Actions:**
1. Push your code to GitHub
2. Add deployment secrets (see `.github/README.md`)
3. Workflows will run automatically!

### Manual Deployment Options

### Using Gunicorn
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

### Environment Variables
- `FLASK_ENV=production` - Set for production
- `FLASK_DEBUG=0` - Disable debug mode

### Health Check
The application includes a health check endpoint at `/` that can be used with load balancers and monitoring tools.

## 📋 Requirements

- Python 3.7+
- Flask 2.3+
- Markdown 3.4+
- PyYAML 6.0+
- Docker (optional)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

**Port already in use:**
```bash
python deploy.py --stop
```

**Dependencies not found:**
```bash
pip install -r requirements.txt
```

**Docker build fails:**
```bash
docker system prune
python deploy.py --build
```

**Permission errors:**
```bash
sudo chown -R $USER:$USER docs/
```

## 🎯 Roadmap

- [ ] User authentication
- [ ] Document versioning
- [ ] Export to PDF
- [ ] Team collaboration features
- [ ] Advanced search filters
- [ ] Custom themes
- [ ] Plugin system
- [x] **GitHub Actions CI/CD** ✅
- [x] **Multi-platform deployment** ✅
- [x] **Automated testing** ✅
- [x] **Security scanning** ✅

---

Built with ❤️ using Flask and modern web technologies.
