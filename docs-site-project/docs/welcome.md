# Welcome to Your Documentation Site! 🎉

This is your brand new documentation platform built with Python Flask!

## What You've Got

✨ **Live Editor** - Write markdown with instant preview  
🔍 **Search** - Find any document quickly  
🐳 **Docker Ready** - Deploy anywhere with Docker  
📱 **Mobile Friendly** - Works on all devices  
🚀 **Easy Deploy** - Automated scripts included  

## Quick Start Guide

### Creating Documents
1. Click "New Document" in the navigation
2. Write your content in Markdown
3. Use the live preview to see changes
4. Save with Ctrl+S (or Cmd+S on Mac)

### Organizing Content
- Use descriptive filenames
- Create an index for navigation  
- Group related documents
- Keep consistent formatting

### Markdown Examples

#### Code Blocks
```python
def hello_world():
    print("Hello from your docs site!")
    return "Welcome! 🎉"
```

#### Lists and Links
- [Create a new document](/new)
- [Search existing docs](/search)
- [View this document source](/edit/welcome)

#### Tables
| Feature | Status | Description |
|---------|--------|-------------|
| Live Editor | ✅ | Real-time markdown preview |
| Search | ✅ | Full-text search |
| Docker | ✅ | Container deployment |
| API | ✅ | RESTful endpoints |

## Deployment Options

### Development
```bash
python app.py
```

### Production with Docker
```bash
python deploy.py --docker
```

### Full Deployment
```bash
python deploy.py --all
```

## Features in Detail

### 📝 Markdown Editor
- **Syntax highlighting** for code blocks
- **Live preview** as you type
- **Auto-save** functionality
- **Keyboard shortcuts** (Ctrl+S to save)

### 🔍 Search System
- **Full-text search** across all documents
- **Fast results** with highlighting
- **Easy navigation** to found content

### 🐳 Docker Integration
- **Ready-to-use** Dockerfile
- **Docker Compose** setup
- **Production ready** with Nginx
- **Volume mounting** for persistent data

### 📊 API Access
Access your docs programmatically:
- `GET /api/docs` - List all documents
- `POST /save` - Save document content
- `GET /search?q=term` - Search documents

## Getting Help

Need assistance? Here are your options:

1. **Check the README** - Comprehensive setup guide
2. **Use the API** - Programmatic access to all features
3. **Docker Support** - Containerized deployment
4. **Search Function** - Find any information quickly

## What's Next?

🎯 **Start documenting!** Create your first custom document  
🔧 **Customize** the site configuration in `site_config.yaml`  
🚀 **Deploy** using Docker for production use  
📈 **Scale** by adding more content and organizing it well  

---

**Pro Tip:** Use the keyboard shortcut `Ctrl+/` (or `Cmd+/`) to quickly focus on the search box!

Happy documenting! 🚀
