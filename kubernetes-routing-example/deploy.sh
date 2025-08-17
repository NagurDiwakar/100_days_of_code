#!/bin/bash

# Kubernetes Routing Example Deployment Script

echo "🚀 Deploying Kubernetes Routing Example..."

# Check if kubectl is available
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl is not installed or not in PATH"
    exit 1
fi

# Check if cluster is accessible
if ! kubectl cluster-info &> /dev/null; then
    echo "❌ Cannot connect to Kubernetes cluster"
    exit 1
fi

echo "✅ Kubernetes cluster is accessible"

# Deploy components in order
echo "📦 Creating namespace..."
kubectl apply -f 01-namespace.yaml

echo "🗄️  Deploying database..."
kubectl apply -f 02-database.yaml

echo "⚙️  Deploying backend API..."
kubectl apply -f 03-backend.yaml

echo "🌐 Deploying frontend..."
kubectl apply -f 04-frontend.yaml

echo "🔀 Setting up ingress routing..."
kubectl apply -f 05-ingress.yaml

echo "🔒 Applying network policies..."
kubectl apply -f 06-network-policies.yaml

echo "⏳ Waiting for deployments to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/postgres-db -n myapp
kubectl wait --for=condition=available --timeout=300s deployment/backend-api -n myapp
kubectl wait --for=condition=available --timeout=300s deployment/frontend-app -n myapp

echo "📊 Checking deployment status..."
kubectl get all -n myapp

echo "🔍 Getting ingress information..."
kubectl get ingress -n myapp

echo "✅ Deployment completed!"
echo ""
echo "🌐 Access your application:"
echo "   Frontend: http://myapp.local/"
echo "   API: http://myapp.local/api/"
echo ""
echo "📝 Add this to your /etc/hosts file:"
echo "   127.0.0.1 myapp.local api.myapp.local"
echo ""
echo "🔧 Useful commands:"
echo "   kubectl get pods -n myapp"
echo "   kubectl logs -f deployment/backend-api -n myapp"
echo "   kubectl describe ingress myapp-ingress -n myapp"
