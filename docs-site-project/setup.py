#!/usr/bin/env python3
"""
Quick setup script for the documentation site
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, check=True):
    """Run shell command"""
    print(f"🔧 Running: {command}")
    try:
        result = subprocess.run(command, shell=True, check=check)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {e}")
        return False

def main():
    print("🚀 Quick Setup - Documentation Site")
    print("=" * 50)
    
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Install Python packages
    print("📦 Installing Python packages...")
    if not run_command("pip install -r requirements.txt"):
        print("❌ Failed to install packages. Trying with user install...")
        run_command("pip install --user -r requirements.txt")
    
    # Create directories
    print("📁 Creating directories...")
    for dir_name in ['docs', 'static/css', 'static/js']:
        Path(dir_name).mkdir(parents=True, exist_ok=True)
    
    # Create sample document if needed
    docs_dir = Path('docs')
    if not list(docs_dir.glob('*.md')):
        print("📝 Creating sample document...")
        sample_content = '''# Welcome to Documentation Site

This is your first document! 🎉

## Features

- ✏️ **Live Editor** - Write and preview markdown in real-time
- 🔍 **Search** - Find documents quickly
- 🐳 **Docker Ready** - Easy deployment
- 📱 **Responsive** - Works on all devices

## Getting Started

1. Edit this document or create a new one
2. Use markdown syntax for formatting
3. Save and share with your team

Happy documenting! 🚀
'''
        with open(docs_dir / 'welcome.md', 'w', encoding='utf-8') as f:
            f.write(sample_content)
    
    print("\n✅ Setup complete!")
    print("\n🚀 Next steps:")
    print("   python app.py                 # Run development server")
    print("   python deploy.py --dev        # Run with deployment manager")
    print("   python deploy.py --docker     # Run with Docker")
    print("\n📱 Then open: http://localhost:5000")

if __name__ == '__main__':
    main()
