"""
Documentation Site - Flask Application
A simple yet powerful documentation site with markdown support
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import markdown
import os
import json
from datetime import datetime
import yaml

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Configuration
DOCS_DIR = 'docs'
CONFIG_FILE = 'site_config.yaml'

class DocumentationSite:
    def __init__(self):
        self.ensure_directories()
        self.load_config()
    
    def ensure_directories(self):
        """Create necessary directories if they don't exist"""
        dirs = [DOCS_DIR, 'static/css', 'static/js', 'templates']
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
    
    def load_config(self):
        """Load site configuration"""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = {
                'site_name': 'Documentation Site',
                'description': 'A modern documentation platform',
                'version': '1.0.0',
                'author': 'Developer'
            }
            self.save_config()
    
    def save_config(self):
        """Save site configuration"""
        with open(CONFIG_FILE, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False)
    
    def get_all_docs(self):
        """Get list of all documentation files"""
        docs = []
        if os.path.exists(DOCS_DIR):
            for file in os.listdir(DOCS_DIR):
                if file.endswith('.md'):
                    file_path = os.path.join(DOCS_DIR, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Extract title from first line if it's a header
                        lines = content.split('\n')
                        title = file.replace('.md', '').replace('_', ' ').title()
                        if lines and lines[0].startswith('#'):
                            title = lines[0].strip('#').strip()
                        
                        docs.append({
                            'filename': file,
                            'title': title,
                            'modified': datetime.fromtimestamp(
                                os.path.getmtime(file_path)
                            ).strftime('%Y-%m-%d %H:%M')
                        })
        return sorted(docs, key=lambda x: x['modified'], reverse=True)
    
    def get_doc_content(self, filename):
        """Get markdown content and convert to HTML"""
        file_path = os.path.join(DOCS_DIR, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                html_content = markdown.markdown(
                    content, 
                    extensions=['codehilite', 'fenced_code', 'tables', 'toc']
                )
                return content, html_content
        return None, None
    
    def save_doc(self, filename, content):
        """Save document content"""
        file_path = os.path.join(DOCS_DIR, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Initialize the documentation site
doc_site = DocumentationSite()

@app.route('/')
def index():
    """Homepage with list of documents"""
    docs = doc_site.get_all_docs()
    return render_template('index.html', docs=docs, config=doc_site.config)

@app.route('/doc/<filename>')
def view_doc(filename):
    """View a specific document"""
    if not filename.endswith('.md'):
        filename += '.md'
    
    raw_content, html_content = doc_site.get_doc_content(filename)
    if html_content:
        return render_template('document.html', 
                             content=html_content, 
                             filename=filename,
                             config=doc_site.config)
    return "Document not found", 404

@app.route('/edit/<filename>')
def edit_doc(filename):
    """Edit a document"""
    if not filename.endswith('.md'):
        filename += '.md'
    
    raw_content, _ = doc_site.get_doc_content(filename)
    return render_template('editor.html', 
                         content=raw_content or '', 
                         filename=filename,
                         config=doc_site.config)

@app.route('/save', methods=['POST'])
def save_doc():
    """Save document content"""
    data = request.get_json()
    filename = data.get('filename')
    content = data.get('content')
    
    if filename and content is not None:
        if not filename.endswith('.md'):
            filename += '.md'
        doc_site.save_doc(filename, content)
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Invalid data'})

@app.route('/new')
def new_doc():
    """Create a new document"""
    return render_template('editor.html', 
                         content='# New Document\n\nStart writing your documentation here...', 
                         filename='new_document.md',
                         config=doc_site.config)

@app.route('/api/docs')
def api_docs():
    """API endpoint to get all documents"""
    return jsonify(doc_site.get_all_docs())

@app.route('/search')
def search():
    """Search functionality"""
    query = request.args.get('q', '')
    results = []
    
    if query:
        docs = doc_site.get_all_docs()
        for doc in docs:
            raw_content, _ = doc_site.get_doc_content(doc['filename'])
            if raw_content and query.lower() in raw_content.lower():
                results.append(doc)
    
    return render_template('search.html', 
                         results=results, 
                         query=query,
                         config=doc_site.config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
