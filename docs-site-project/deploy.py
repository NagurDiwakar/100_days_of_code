#!/usr/bin/env python3
"""
Documentation Site Deployment Manager
Automates building, testing, and deploying the documentation site
"""

import os
import sys
import subprocess
import json
import time
import argparse
from pathlib import Path
import yaml

class DocsSiteManager:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else Path(__file__).parent
        self.config_file = self.project_dir / 'site_config.yaml'
        self.load_config()
    
    def load_config(self):
        """Load deployment configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = {
                'site_name': 'Documentation Site',
                'description': 'A modern documentation platform',
                'version': '1.0.0',
                'author': 'Developer',
                'docker': {
                    'image_name': 'docs-site',
                    'container_name': 'docs-site-app',
                    'port': 5000
                },
                'deployment': {
                    'environment': 'local',
                    'auto_restart': True
                }
            }
            self.save_config()
    
    def save_config(self):
        """Save configuration"""
        with open(self.config_file, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False)
    
    def run_command(self, command, check=True, capture_output=False):
        """Run shell command with proper error handling"""
        print(f"🔧 Running: {command}")
        try:
            if capture_output:
                result = subprocess.run(command, shell=True, check=check, 
                                      capture_output=True, text=True, 
                                      cwd=self.project_dir)
                return result.stdout.strip()
            else:
                result = subprocess.run(command, shell=True, check=check, cwd=self.project_dir)
                return result.returncode == 0
        except subprocess.CalledProcessError as e:
            print(f"❌ Command failed: {e}")
            return False
    
    def setup_environment(self):
        """Set up local development environment"""
        print("🚀 Setting up development environment...")
        
        # Create virtual environment if it doesn't exist
        venv_path = self.project_dir / 'venv'
        if not venv_path.exists():
            print("📦 Creating virtual environment...")
            self.run_command(f"python3 -m venv {venv_path}")
        
        # Install requirements
        print("📦 Installing Python packages...")
        pip_cmd = f"{venv_path}/bin/pip" if os.name != 'nt' else f"{venv_path}\\Scripts\\pip"
        self.run_command(f"{pip_cmd} install -r requirements.txt")
        
        # Create necessary directories
        for dir_name in ['docs', 'static/css', 'static/js']:
            dir_path = self.project_dir / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Create sample document if docs is empty
        docs_dir = self.project_dir / 'docs'
        if not list(docs_dir.glob('*.md')):
            self.create_sample_docs()
        
        print("✅ Environment setup complete!")
    
    def create_sample_docs(self):
        """Create sample documentation"""
        print("📝 Creating sample documentation...")
        
        sample_docs = [
            {
                'filename': 'getting_started.md',
                'content': '''# Getting Started

Welcome to the Documentation Site! This is a powerful platform for creating and managing documentation.

## Features

- 📝 **Markdown Editor** - Write docs in markdown with live preview
- 🔍 **Search** - Full-text search across all documents
- 🐳 **Docker Support** - Easy deployment with Docker
- 🚀 **Auto-deployment** - Automated build and deploy scripts
- 📱 **Responsive Design** - Works on all devices

## Quick Start

1. Create a new document using the "New Document" button
2. Write your content in Markdown format
3. Save and view your document
4. Share with your team!

## Markdown Syntax

### Headers
```markdown
# H1 Header
## H2 Header
### H3 Header
```

### Text Formatting
- **Bold text**
- *Italic text*
- `Inline code`

### Lists
1. First item
2. Second item
3. Third item

### Code Blocks
```python
def hello_world():
    print("Hello, World!")
```

### Links and Images
[Link text](https://example.com)
![Image alt text](image.jpg)

Happy documenting! 🎉
'''
            },
            {
                'filename': 'api_reference.md',
                'content': '''# API Reference

This documentation site provides several API endpoints for programmatic access.

## Endpoints

### GET /api/docs
Returns a list of all documents.

**Response:**
```json
[
  {
    "filename": "document.md",
    "title": "Document Title",
    "modified": "2025-08-30 10:30"
  }
]
```

### POST /save
Save a document.

**Request Body:**
```json
{
  "filename": "document.md",
  "content": "# Document content..."
}
```

**Response:**
```json
{
  "success": true
}
```

### GET /search?q=query
Search for documents containing the query.

**Parameters:**
- `q` - Search query string

## Authentication

Currently, no authentication is required for the API endpoints.

## Rate Limiting

No rate limiting is currently implemented.
'''
            },
            {
                'filename': 'deployment_guide.md',
                'content': '''# Deployment Guide

Learn how to deploy your documentation site in different environments.

## Local Development

1. **Setup Environment:**
   ```bash
   python deploy.py --setup
   ```

2. **Run Development Server:**
   ```bash
   python deploy.py --dev
   ```

3. **Access the site:**
   Open http://localhost:5000

## Docker Deployment

1. **Build Docker Image:**
   ```bash
   python deploy.py --build
   ```

2. **Run with Docker:**
   ```bash
   python deploy.py --docker
   ```

3. **Using Docker Compose:**
   ```bash
   docker-compose up -d
   ```

## Production Deployment

### Using Gunicorn
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

### Using Docker in Production
```bash
docker run -d -p 80:5000 --name docs-site docs-site:latest
```

### Environment Variables
- `FLASK_ENV` - Set to 'production' for production
- `FLASK_DEBUG` - Set to '0' for production

## Monitoring

The application includes health checks at `/` endpoint.

## Backup

Regularly backup your `docs/` directory and `site_config.yaml` file.
'''
            }
        ]
        
        for doc in sample_docs:
            doc_path = self.project_dir / 'docs' / doc['filename']
            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(doc['content'])
        
        print(f"✅ Created {len(sample_docs)} sample documents")
    
    def run_dev_server(self):
        """Run development server"""
        print("🚀 Starting development server...")
        
        # Check if virtual environment exists
        venv_path = self.project_dir / 'venv'
        if venv_path.exists():
            python_cmd = f"{venv_path}/bin/python" if os.name != 'nt' else f"{venv_path}\\Scripts\\python"
        else:
            python_cmd = "python3"
        
        # Set environment variables
        env = os.environ.copy()
        env['FLASK_ENV'] = 'development'
        env['FLASK_DEBUG'] = '1'
        
        print("📱 Server will be available at: http://localhost:5000")
        print("🛑 Press Ctrl+C to stop the server")
        
        try:
            subprocess.run([python_cmd, 'app.py'], env=env, cwd=self.project_dir)
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")
    
    def build_docker_image(self):
        """Build Docker image"""
        print("🐳 Building Docker image...")
        
        image_name = self.config['docker']['image_name']
        version = self.config['version']
        
        # Build image
        success = self.run_command(f"docker build -t {image_name}:{version} -t {image_name}:latest .")
        
        if success:
            print(f"✅ Docker image built: {image_name}:{version}")
            return True
        else:
            print("❌ Docker build failed")
            return False
    
    def run_docker_container(self):
        """Run Docker container"""
        print("🐳 Running Docker container...")
        
        container_name = self.config['docker']['container_name']
        image_name = self.config['docker']['image_name']
        port = self.config['docker']['port']
        
        # Stop existing container if running
        self.run_command(f"docker stop {container_name}", check=False)
        self.run_command(f"docker rm {container_name}", check=False)
        
        # Run new container
        cmd = f"""docker run -d 
                 --name {container_name} 
                 -p {port}:5000 
                 -v {self.project_dir}/docs:/app/docs 
                 -v {self.project_dir}/site_config.yaml:/app/site_config.yaml 
                 --restart unless-stopped 
                 {image_name}:latest"""
        
        success = self.run_command(cmd.replace('\n', ' ').strip())
        
        if success:
            print(f"✅ Container running: http://localhost:{port}")
            print(f"🐳 Container name: {container_name}")
            return True
        else:
            print("❌ Failed to run Docker container")
            return False
    
    def deploy_with_compose(self):
        """Deploy using Docker Compose"""
        print("🐳 Deploying with Docker Compose...")
        
        # Build and run with compose
        success = self.run_command("docker-compose up -d --build")
        
        if success:
            print("✅ Deployed with Docker Compose")
            print("📱 Site available at: http://localhost:5000")
            print("🌐 Nginx proxy at: http://localhost:80")
            return True
        else:
            print("❌ Docker Compose deployment failed")
            return False
    
    def stop_services(self):
        """Stop all running services"""
        print("🛑 Stopping services...")
        
        # Stop Docker container
        container_name = self.config['docker']['container_name']
        self.run_command(f"docker stop {container_name}", check=False)
        
        # Stop Docker Compose
        self.run_command("docker-compose down", check=False)
        
        print("✅ Services stopped")
    
    def show_status(self):
        """Show deployment status"""
        print("📊 Deployment Status:")
        print("-" * 40)
        
        # Check Docker container
        container_name = self.config['docker']['container_name']
        status = self.run_command(f"docker ps --filter name={container_name} --format '{{{{.Status}}}}'", 
                                capture_output=True)
        if status:
            print(f"🐳 Docker Container: Running ({status})")
        else:
            print("🐳 Docker Container: Not running")
        
        # Check Docker Compose
        compose_status = self.run_command("docker-compose ps", capture_output=True)
        if "Up" in compose_status:
            print("🐙 Docker Compose: Running")
        else:
            print("🐙 Docker Compose: Not running")
        
        # Show configuration
        print(f"\n⚙️  Configuration:")
        print(f"   Site Name: {self.config['site_name']}")
        print(f"   Version: {self.config['version']}")
        print(f"   Port: {self.config['docker']['port']}")
        
        # Count documents
        docs_dir = self.project_dir / 'docs'
        doc_count = len(list(docs_dir.glob('*.md'))) if docs_dir.exists() else 0
        print(f"   Documents: {doc_count}")
    
    def run_tests(self):
        """Run basic tests"""
        print("🧪 Running tests...")
        
        # Check if required files exist
        required_files = ['app.py', 'requirements.txt', 'Dockerfile', 'docker-compose.yml']
        for file in required_files:
            if not (self.project_dir / file).exists():
                print(f"❌ Missing required file: {file}")
                return False
        
        # Test if app can be imported
        try:
            sys.path.insert(0, str(self.project_dir))
            import app
            print("✅ App module can be imported")
        except ImportError as e:
            print(f"❌ Cannot import app: {e}")
            return False
        
        print("✅ All tests passed")
        return True


def main():
    parser = argparse.ArgumentParser(description='Documentation Site Deployment Manager')
    parser.add_argument('--setup', action='store_true', help='Setup development environment')
    parser.add_argument('--dev', action='store_true', help='Run development server')
    parser.add_argument('--build', action='store_true', help='Build Docker image')
    parser.add_argument('--docker', action='store_true', help='Run Docker container')
    parser.add_argument('--compose', action='store_true', help='Deploy with Docker Compose')
    parser.add_argument('--stop', action='store_true', help='Stop all services')
    parser.add_argument('--status', action='store_true', help='Show deployment status')
    parser.add_argument('--test', action='store_true', help='Run tests')
    parser.add_argument('--all', action='store_true', help='Setup, build, and deploy')
    
    args = parser.parse_args()
    
    manager = DocsSiteManager()
    
    if args.setup or args.all:
        manager.setup_environment()
    
    if args.test:
        if not manager.run_tests():
            sys.exit(1)
    
    if args.build or args.all:
        if not manager.build_docker_image():
            sys.exit(1)
    
    if args.docker or args.all:
        if not manager.run_docker_container():
            sys.exit(1)
    
    if args.compose:
        if not manager.deploy_with_compose():
            sys.exit(1)
    
    if args.dev:
        manager.run_dev_server()
    
    if args.stop:
        manager.stop_services()
    
    if args.status:
        manager.show_status()
    
    if not any(vars(args).values()):
        print("📚 Documentation Site Deployment Manager")
        print("Use --help to see available options")
        print("\n🚀 Quick start:")
        print("  python deploy.py --setup    # Setup environment")
        print("  python deploy.py --dev      # Run development server")
        print("  python deploy.py --all      # Full deployment")


if __name__ == '__main__':
    main()
