# GitHub Actions Setup Guide

This document explains how to configure GitHub Actions for automated deployment of your documentation site.

## 📋 Overview

The repository includes several GitHub Actions workflows:

- **🧪 Test & Quality Check** (`test.yml`) - Runs tests, linting, and security scans
- **🐳 Docker Build** (`docker.yml`) - Builds and pushes Docker images
- **📦 Release** (`release.yml`) - Creates GitHub releases with packages
- **🌐 Cloud Deploy** (`deploy-cloud.yml`) - Deploys to various cloud platforms
- **🚀 Main Deploy** (`deploy.yml`) - Comprehensive deployment pipeline

## ⚙️ Required Secrets

To enable automatic deployment, you need to configure the following secrets in your GitHub repository:

### Navigation to Secrets
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**

### 🔐 Required Secrets by Platform

#### For Docker Registry (GitHub Container Registry)
- **GITHUB_TOKEN** - Automatically provided by GitHub (no setup needed)

#### For Heroku Deployment
```
HEROKU_API_KEY - Your Heroku API key
HEROKU_APP_NAME - Your Heroku app name
HEROKU_EMAIL - Your Heroku account email
```

#### For AWS ECS Deployment
```
AWS_ACCESS_KEY_ID - AWS access key
AWS_SECRET_ACCESS_KEY - AWS secret key
AWS_REGION - AWS region (e.g., us-east-1)
ECS_CLUSTER_NAME - ECS cluster name
ECS_SERVICE_NAME - ECS service name
ECS_EXECUTION_ROLE_ARN - ECS execution role ARN
ECS_TASK_ROLE_ARN - ECS task role ARN
```

#### For Digital Ocean Deployment
```
DO_ACCESS_TOKEN - Digital Ocean access token
DO_APP_NAME - Digital Ocean app name
```

#### For Railway Deployment
```
RAILWAY_TOKEN - Railway authentication token
```

#### For Fly.io Deployment
```
FLY_API_TOKEN - Fly.io API token
```

#### For Self-Hosted Server Deployment
```
HOST - Server hostname or IP
USERNAME - SSH username
SSH_PRIVATE_KEY - SSH private key
PORT - SSH port (optional, defaults to 22)
```

## 🚀 Workflow Triggers

### Automatic Triggers
- **Push to main/master** - Triggers build, test, and deployment
- **Pull Requests** - Triggers tests and builds (no deployment)
- **Tags (v\*)** - Triggers release creation

### Manual Triggers
- **Manual Deploy** - Use GitHub Actions tab → "Deploy to Cloud Platforms"
- **Manual Release** - Use GitHub Actions tab → "Release"

## 📝 Setup Instructions

### 1. Enable GitHub Actions
1. Go to your repository
2. Click **Actions** tab
3. Choose **"I understand my workflows and want to enable them"**

### 2. Configure Secrets
Add the secrets for your chosen deployment platform(s) as described above.

### 3. Configure Environments (Optional)
1. Go to **Settings** → **Environments**
2. Create environments: `staging`, `production`
3. Add environment-specific secrets
4. Set up protection rules (e.g., require reviews for production)

### 4. Customize Workflows
Edit the workflow files in `.github/workflows/` to match your needs:

- Change deployment targets
- Modify build steps
- Update notification settings
- Add additional testing

## 🔧 Platform-Specific Setup

### Heroku Setup
1. Install Heroku CLI
2. Create app: `heroku create your-docs-site`
3. Get API key: `heroku auth:token`
4. Add secrets to GitHub

### AWS ECS Setup
1. Create ECS cluster
2. Create task definition
3. Create service
4. Set up IAM roles
5. Add AWS credentials to GitHub secrets

### Digital Ocean Setup
1. Create Digital Ocean account
2. Generate API token
3. Create app in App Platform
4. Add token to GitHub secrets

### Railway Setup
1. Create Railway account
2. Generate deployment token
3. Connect GitHub repository
4. Add token to GitHub secrets

### Self-Hosted Setup
1. Prepare server with Docker installed
2. Generate SSH key pair
3. Add public key to server
4. Add private key to GitHub secrets

## 📊 Monitoring Deployments

### GitHub Actions Dashboard
- Monitor workflow runs in the **Actions** tab
- View logs for debugging
- Check deployment status

### Health Checks
The workflows include automatic health checks:
- Container startup verification
- HTTP endpoint testing
- Service availability checks

### Notifications
Configure notifications for:
- Successful deployments
- Failed deployments
- Security alerts

## 🛠️ Troubleshooting

### Common Issues

#### "Secret not found" Error
- Verify secret names match exactly
- Check environment restrictions
- Ensure secrets are set at repository level

#### Docker Build Failures
- Check Dockerfile syntax
- Verify base image availability
- Review build logs in Actions tab

#### Deployment Timeouts
- Increase timeout values in workflows
- Check resource availability on target platform
- Verify health check endpoints

#### Permission Errors
- Verify GitHub token permissions
- Check cloud platform IAM roles
- Ensure SSH key permissions

### Debug Steps
1. Check workflow logs in GitHub Actions
2. Verify all required secrets are set
3. Test deployment locally first
4. Check platform-specific documentation

## 🔄 Workflow Customization

### Adding New Deployment Targets
1. Copy existing job in workflow file
2. Modify deployment commands
3. Add required secrets
4. Test with manual trigger

### Custom Build Steps
Add steps to workflows:
```yaml
- name: Custom Build Step
  run: |
    echo "Running custom build..."
    # Your custom commands here
```

### Environment Variables
Set environment variables in workflows:
```yaml
env:
  CUSTOM_VAR: value
  NODE_ENV: production
```

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Hub Documentation](https://docs.docker.com/docker-hub/)
- [Heroku Deployment Guide](https://devcenter.heroku.com/articles/github-integration)
- [AWS ECS Guide](https://docs.aws.amazon.com/ecs/)
- [Digital Ocean App Platform](https://docs.digitalocean.com/products/app-platform/)

## 🎯 Best Practices

1. **Test Locally First** - Always test deployments locally before pushing
2. **Use Environments** - Separate staging and production environments
3. **Monitor Costs** - Keep track of cloud platform usage
4. **Secure Secrets** - Never commit secrets to code
5. **Regular Updates** - Keep workflow actions up to date
6. **Backup Strategy** - Have rollback plans for failed deployments

---

Need help? Check the [main README](README.md) or [open an issue](https://github.com/your-repo/issues).
