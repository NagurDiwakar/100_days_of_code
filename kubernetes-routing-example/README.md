# Kubernetes Routing Example

This example demonstrates various Kubernetes routing scenarios with a simple web application.

## Architecture Overview

```
Internet
    ↓
Load Balancer (LoadBalancer Service)
    ↓
Ingress Controller (NGINX)
    ↓
Backend Services (ClusterIP)
    ↓
Pods (Web App + Database)
```

## Components

1. **Frontend Service** - Web application
2. **Backend API Service** - REST API
3. **Database Service** - PostgreSQL
4. **Ingress** - External routing
5. **Network Policies** - Security rules

## Deployment Order

1. Apply namespace
2. Deploy database
3. Deploy backend API
4. Deploy frontend
5. Apply ingress
6. Apply network policies

## Testing

After deployment, access the application at:
- Frontend: `http://myapp.local/`
- API: `http://myapp.local/api/health`

## Traffic Flow

1. External request → Load Balancer
2. Load Balancer → Ingress Controller
3. Ingress Controller → Frontend/Backend Service
4. Service → Pod (via kube-proxy)
5. Backend Pod → Database Service → Database Pod
