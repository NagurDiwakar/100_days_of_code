#!/bin/bash

# Cleanup script for Kubernetes Routing Example

echo "🧹 Cleaning up Kubernetes Routing Example..."

echo "🗑️  Removing network policies..."
kubectl delete -f 06-network-policies.yaml --ignore-not-found=true

echo "🗑️  Removing ingress..."
kubectl delete -f 05-ingress.yaml --ignore-not-found=true

echo "🗑️  Removing frontend..."
kubectl delete -f 04-frontend.yaml --ignore-not-found=true

echo "🗑️  Removing backend..."
kubectl delete -f 03-backend.yaml --ignore-not-found=true

echo "🗑️  Removing database..."
kubectl delete -f 02-database.yaml --ignore-not-found=true

echo "🗑️  Removing namespace..."
kubectl delete -f 01-namespace.yaml --ignore-not-found=true

echo "✅ Cleanup completed!"
