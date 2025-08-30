#!/usr/bin/env python3
"""
GitHub Actions Integration Script
Provides local testing and validation for GitHub Actions workflows
"""

import os
import sys
import json
import subprocess
import yaml
from pathlib import Path
import argparse

class GitHubActionsHelper:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else Path(__file__).parent
        self.workflows_dir = self.project_dir / '.github' / 'workflows'
        
    def validate_workflows(self):
        """Validate GitHub Actions workflow files"""
        print("🔍 Validating GitHub Actions workflows...")
        
        if not self.workflows_dir.exists():
            print("❌ No .github/workflows directory found")
            return False
            
        workflow_files = list(self.workflows_dir.glob('*.yml')) + list(self.workflows_dir.glob('*.yaml'))
        
        if not workflow_files:
            print("❌ No workflow files found")
            return False
            
        valid_workflows = 0
        for workflow_file in workflow_files:
            try:
                with open(workflow_file, 'r') as f:
                    workflow_data = yaml.safe_load(f)
                    
                if 'name' in workflow_data and (True in workflow_data or 'on' in workflow_data) and 'jobs' in workflow_data:
                    print(f"✅ {workflow_file.name} - Valid workflow")
                    valid_workflows += 1
                else:
                    print(f"❌ {workflow_file.name} - Missing required fields")
                    
            except yaml.YAMLError as e:
                print(f"❌ {workflow_file.name} - YAML syntax error: {e}")
            except Exception as e:
                print(f"❌ {workflow_file.name} - Error: {e}")
                
        print(f"\n📊 Validation Summary: {valid_workflows}/{len(workflow_files)} workflows valid")
        return valid_workflows == len(workflow_files)
    
    def check_secrets_template(self):
        """Check if all required secrets are documented"""
        print("🔐 Checking secrets documentation...")
        
        required_secrets = {
            'heroku': ['HEROKU_API_KEY', 'HEROKU_APP_NAME', 'HEROKU_EMAIL'],
            'aws': ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_REGION', 
                   'ECS_CLUSTER_NAME', 'ECS_SERVICE_NAME'],
            'digital_ocean': ['DO_ACCESS_TOKEN', 'DO_APP_NAME'],
            'railway': ['RAILWAY_TOKEN'],
            'fly_io': ['FLY_API_TOKEN'],
            'self_hosted': ['HOST', 'USERNAME', 'SSH_PRIVATE_KEY']
        }
        
        readme_path = self.project_dir / '.github' / 'README.md'
        
        if readme_path.exists():
            with open(readme_path, 'r') as f:
                readme_content = f.read()
                
            documented_secrets = []
            for platform, secrets in required_secrets.items():
                for secret in secrets:
                    if secret in readme_content:
                        documented_secrets.append(secret)
                        
            total_secrets = sum(len(secrets) for secrets in required_secrets.values())
            print(f"📝 Documented secrets: {len(documented_secrets)}/{total_secrets}")
            
            if len(documented_secrets) < total_secrets:
                print("⚠️  Some secrets may not be documented")
                
        else:
            print("❌ GitHub Actions README not found")
            
    def test_docker_build(self):
        """Test Docker build locally"""
        print("🐳 Testing Docker build...")
        
        dockerfile_path = self.project_dir / 'Dockerfile'
        if not dockerfile_path.exists():
            print("❌ Dockerfile not found")
            return False
            
        try:
            # Build image
            result = subprocess.run([
                'docker', 'build', '-t', 'docs-site-test', '.'
            ], cwd=self.project_dir, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Docker build successful")
                
                # Test container
                test_result = subprocess.run([
                    'docker', 'run', '--rm', '-d', '--name', 'test-container',
                    '-p', '5001:5000', 'docs-site-test'
                ], capture_output=True, text=True)
                
                if test_result.returncode == 0:
                    print("✅ Container started successfully")
                    
                    # Cleanup
                    subprocess.run(['docker', 'stop', 'test-container'], 
                                 capture_output=True)
                    return True
                else:
                    print(f"❌ Container failed to start: {test_result.stderr}")
                    
            else:
                print(f"❌ Docker build failed: {result.stderr}")
                
        except FileNotFoundError:
            print("❌ Docker not found. Please install Docker to test builds.")
            
        return False
    
    def simulate_github_actions(self):
        """Simulate GitHub Actions workflow steps locally"""
        print("🔄 Simulating GitHub Actions workflow...")
        
        # Simulate test job
        print("\n🧪 Simulating test job...")
        try:
            # Install dependencies
            subprocess.run([
                sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
            ], cwd=self.project_dir, check=True, capture_output=True)
            print("✅ Dependencies installed")
            
            # Run basic import test
            subprocess.run([
                sys.executable, '-c', 'import app; print("✅ App import successful")'
            ], cwd=self.project_dir, check=True)
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Test simulation failed: {e}")
            return False
            
        # Simulate build job
        print("\n🏗️ Simulating build job...")
        try:
            # Create deployment package
            package_name = f"docs-site-test.tar.gz"
            subprocess.run([
                'tar', '-czf', package_name,
                '--exclude=.git',
                '--exclude=__pycache__',
                '--exclude=*.pyc',
                '.'
            ], cwd=self.project_dir, check=True, capture_output=True)
            
            print(f"✅ Deployment package created: {package_name}")
            
            # Cleanup
            package_path = self.project_dir / package_name
            if package_path.exists():
                package_path.unlink()
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Build simulation failed: {e}")
            return False
            
        print("✅ Workflow simulation completed successfully")
        return True
    
    def generate_deployment_guide(self):
        """Generate a deployment guide based on available workflows"""
        print("📝 Generating deployment guide...")
        
        guide_content = """# Automated Deployment Guide

## 🚀 Available Deployment Options

Your repository is configured with the following automated deployment workflows:

"""
        
        workflows = {
            'test.yml': '🧪 **Test & Quality Check** - Runs on every push and PR',
            'docker.yml': '🐳 **Docker Build** - Builds and pushes Docker images',
            'release.yml': '📦 **Release Management** - Creates GitHub releases',
            'deploy-cloud.yml': '🌐 **Cloud Deployment** - Deploys to various platforms',
            'deploy.yml': '🚀 **Main Pipeline** - Comprehensive CI/CD pipeline'
        }
        
        for workflow_file, description in workflows.items():
            workflow_path = self.workflows_dir / workflow_file
            if workflow_path.exists():
                guide_content += f"- {description}\n"
                
        guide_content += """
## 🔧 Quick Setup

### 1. Enable GitHub Actions
1. Go to your repository's **Actions** tab
2. Enable workflows if prompted

### 2. Configure Secrets
Add required secrets in **Settings** → **Secrets and variables** → **Actions**

### 3. Trigger Deployment
- **Automatic**: Push to main branch
- **Manual**: Use Actions tab → "Deploy to Cloud Platforms"

## 📚 Platform-Specific Guides

Check `.github/README.md` for detailed setup instructions for each platform.

## 🔍 Monitoring

- Monitor deployments in the **Actions** tab
- Check logs for troubleshooting
- Set up notifications for failures

---

Generated by GitHub Actions Helper
"""
        
        guide_path = self.project_dir / 'DEPLOYMENT_GUIDE.md'
        with open(guide_path, 'w') as f:
            f.write(guide_content)
            
        print(f"✅ Deployment guide created: {guide_path}")
    
    def check_repository_settings(self):
        """Check if repository is properly configured for GitHub Actions"""
        print("⚙️ Checking repository configuration...")
        
        checks = []
        
        # Check if .github directory exists
        if (self.project_dir / '.github').exists():
            checks.append("✅ .github directory exists")
        else:
            checks.append("❌ .github directory missing")
            
        # Check if workflows directory exists
        if self.workflows_dir.exists():
            checks.append("✅ workflows directory exists")
        else:
            checks.append("❌ workflows directory missing")
            
        # Check for important files
        important_files = [
            'Dockerfile',
            'docker-compose.yml',
            'requirements.txt',
            'app.py'
        ]
        
        for file in important_files:
            if (self.project_dir / file).exists():
                checks.append(f"✅ {file} exists")
            else:
                checks.append(f"❌ {file} missing")
                
        # Check for security files
        security_files = ['SECURITY.md', '.github/README.md']
        for file in security_files:
            if (self.project_dir / file).exists():
                checks.append(f"✅ {file} exists")
            else:
                checks.append(f"⚠️  {file} recommended")
                
        print("\n📋 Repository Configuration:")
        for check in checks:
            print(f"  {check}")
            
        return all("✅" in check for check in checks if "❌" in check)


def main():
    parser = argparse.ArgumentParser(description='GitHub Actions Helper for Documentation Site')
    parser.add_argument('--validate', action='store_true', help='Validate workflow files')
    parser.add_argument('--test-docker', action='store_true', help='Test Docker build')
    parser.add_argument('--simulate', action='store_true', help='Simulate GitHub Actions locally')
    parser.add_argument('--check-secrets', action='store_true', help='Check secrets documentation')
    parser.add_argument('--generate-guide', action='store_true', help='Generate deployment guide')
    parser.add_argument('--check-config', action='store_true', help='Check repository configuration')
    parser.add_argument('--all', action='store_true', help='Run all checks')
    
    args = parser.parse_args()
    
    helper = GitHubActionsHelper()
    
    if args.all:
        args.validate = True
        args.test_docker = True
        args.simulate = True
        args.check_secrets = True
        args.generate_guide = True
        args.check_config = True
    
    success = True
    
    if args.check_config:
        if not helper.check_repository_settings():
            success = False
    
    if args.validate:
        if not helper.validate_workflows():
            success = False
    
    if args.check_secrets:
        helper.check_secrets_template()
    
    if args.test_docker:
        if not helper.test_docker_build():
            success = False
    
    if args.simulate:
        if not helper.simulate_github_actions():
            success = False
    
    if args.generate_guide:
        helper.generate_deployment_guide()
    
    if not any(vars(args).values()):
        print("🤖 GitHub Actions Helper for Documentation Site")
        print("Use --help to see available options")
        print("\n🚀 Quick commands:")
        print("  python github_actions_helper.py --all          # Run all checks")
        print("  python github_actions_helper.py --validate     # Validate workflows")
        print("  python github_actions_helper.py --simulate     # Test locally")
    
    if success:
        print("\n🎉 All checks passed! Your repository is ready for GitHub Actions.")
    else:
        print("\n⚠️  Some issues found. Please address them before deployment.")
        sys.exit(1)


if __name__ == '__main__':
    main()
