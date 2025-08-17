# Complete Example: E-commerce Application Routing

## Architecture Overview

```
Internet → DNS → Load Balancer → Ingress Controller → Services → Pods
```

## External DNS Request Flow Example

### User Request: `https://api.mystore.com/orders/123`

#### Step 1: DNS Resolution
```bash
# User's browser/client performs DNS lookup
dig api.mystore.com

# DNS response:
# api.mystore.com    300    IN    A    203.0.113.10
```

#### Step 2: Load Balancer Routing
```
Client Request:
  Host: api.mystore.com
  Path: /orders/123
  Method: GET
  ↓
Load Balancer (203.0.113.10):
  Routes to Ingress Controller Pod IP: 10.244.1.15:80
```

#### Step 3: Ingress Controller Processing
```
NGINX Ingress Controller:
  1. Receives request on port 80
  2. Checks Host header: "api.mystore.com"
  3. Checks Path: "/orders/123"
  4. Matches ingress rule
  5. Routes to backend service: "orders-service:80"
```

#### Step 4: Service Load Balancing
```
orders-service (ClusterIP: 10.96.100.50):
  1. Receives request from ingress controller
  2. kube-proxy applies iptables rules
  3. Load balances to one of 3 available pods:
     - orders-backend-pod-1 (10.244.1.20:8080)
     - orders-backend-pod-2 (10.244.2.21:8080)
     - orders-backend-pod-3 (10.244.3.22:8080)
  4. Selects: orders-backend-pod-2
```

#### Step 5: Pod Processing
```
orders-backend-pod-2:
  1. Receives HTTP request on port 8080
  2. Application processes order lookup for ID 123
  3. Queries database service: database-service.default.svc.cluster.local
  4. Returns order data as JSON response
```

## Ingress Routing Types Explained

### Path-Based Routing: Single Domain, Multiple Services

**Domain**: `api.mystore.com`

```
/orders/*     → Orders Service     (Order management)
/users/*      → Users Service      (User management)
/products/*   → Products Service   (Product catalog)
/payments/*   → Payments Service   (Payment processing)
/inventory/*  → Inventory Service  (Stock management)
```

**Example URLs**:
- `api.mystore.com/orders/123` → Get order details
- `api.mystore.com/users/profile` → Get user profile
- `api.mystore.com/products/search?q=laptop` → Search products
- `api.mystore.com/payments/process` → Process payment
- `api.mystore.com/inventory/check/item-456` → Check stock

### Host-Based Routing: Multiple Domains, Different Services

```
orders.mystore.com    → Orders Application    (Complete orders app)
admin.mystore.com     → Admin Panel          (Management interface)
api.mystore.com       → API Gateway          (Public API)
dashboard.mystore.com → Analytics Dashboard  (Business metrics)
```

**Example URLs**:
- `orders.mystore.com` → Customer order tracking interface
- `admin.mystore.com` → Administrative dashboard
- `api.mystore.com/v1/orders` → REST API endpoint
- `dashboard.mystore.com` → Business analytics

### Combined Routing: Both Host and Path

```
api.mystore.com/v1/orders      → Orders API v1
api.mystore.com/v2/orders      → Orders API v2
api.mystore.com/v1/users       → Users API v1

admin.mystore.com/orders       → Orders admin panel
admin.mystore.com/users        → Users admin panel
admin.mystore.com/analytics    → Analytics admin panel

app.mystore.com/orders         → Customer orders UI
app.mystore.com/profile        → Customer profile UI
app.mystore.com/cart           → Shopping cart UI
```

## Key Clarifications

### Host-Based Routing is NOT About Deployments
❌ **Wrong Understanding**: "Host-based means different deployments/instances of the same app"

✅ **Correct Understanding**: "Host-based means different domains routing to different services/applications"

### Different Deployments Example
If you want different deployments (staging vs production), you use:

```
# Different namespaces
orders-service.production.svc.cluster.local
orders-service.staging.svc.cluster.local

# Different domains
api.mystore.com           → Production
staging-api.mystore.com   → Staging
dev-api.mystore.com       → Development

# Different clusters entirely
prod-cluster.mystore.com
staging-cluster.mystore.com
```

## Complete Working Example

### 1. Namespace
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ecommerce
```

### 2. Applications (Deployments)
```yaml
# Orders Service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-backend
  namespace: ecommerce
spec:
  replicas: 3
  selector:
    matchLabels:
      app: orders-backend
  template:
    metadata:
      labels:
        app: orders-backend
    spec:
      containers:
      - name: orders
        image: mystore/orders-api:v1.0
        ports:
        - containerPort: 8080
---
# Users Service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: users-backend
  namespace: ecommerce
spec:
  replicas: 2
  selector:
    matchLabels:
      app: users-backend
  template:
    metadata:
      labels:
        app: users-backend
    spec:
      containers:
      - name: users
        image: mystore/users-api:v1.0
        ports:
        - containerPort: 8080
---
# Admin Panel
apiVersion: apps/v1
kind: Deployment
metadata:
  name: admin-panel
  namespace: ecommerce
spec:
  replicas: 1
  selector:
    matchLabels:
      app: admin-panel
  template:
    metadata:
      labels:
        app: admin-panel
    spec:
      containers:
      - name: admin
        image: mystore/admin-panel:v1.0
        ports:
        - containerPort: 3000
```

### 3. Services
```yaml
# Orders Service
apiVersion: v1
kind: Service
metadata:
  name: orders-service
  namespace: ecommerce
spec:
  selector:
    app: orders-backend
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP
---
# Users Service
apiVersion: v1
kind: Service
metadata:
  name: users-service
  namespace: ecommerce
spec:
  selector:
    app: users-backend
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP
---
# Admin Service
apiVersion: v1
kind: Service
metadata:
  name: admin-service
  namespace: ecommerce
spec:
  selector:
    app: admin-panel
  ports:
  - port: 80
    targetPort: 3000
  type: ClusterIP
```

### 4. Ingress with Combined Routing
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ecommerce-ingress
  namespace: ecommerce
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  tls:
  - hosts:
    - api.mystore.com
    - admin.mystore.com
    secretName: mystore-tls
  rules:
  # API routing (path-based)
  - host: api.mystore.com
    http:
      paths:
      - path: /orders
        pathType: Prefix
        backend:
          service:
            name: orders-service
            port:
              number: 80
      - path: /users
        pathType: Prefix
        backend:
          service:
            name: users-service
            port:
              number: 80
  # Admin routing (host-based)
  - host: admin.mystore.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: admin-service
            port:
              number: 80
```

## Traffic Flow Examples

### Example 1: API Request
```
Request: GET https://api.mystore.com/orders/123
Flow:
  1. DNS: api.mystore.com → 203.0.113.10
  2. Load Balancer → Ingress Controller
  3. Host: api.mystore.com, Path: /orders/123
  4. Routes to: orders-service
  5. Service routes to: orders-backend pod
  6. Response: Order details JSON
```

### Example 2: Admin Panel
```
Request: GET https://admin.mystore.com/dashboard
Flow:
  1. DNS: admin.mystore.com → 203.0.113.10
  2. Load Balancer → Ingress Controller
  3. Host: admin.mystore.com, Path: /dashboard
  4. Routes to: admin-service
  5. Service routes to: admin-panel pod
  6. Response: Admin dashboard HTML
```

### Example 3: User Management
```
Request: POST https://api.mystore.com/users/register
Flow:
  1. DNS: api.mystore.com → 203.0.113.10
  2. Load Balancer → Ingress Controller
  3. Host: api.mystore.com, Path: /users/register
  4. Routes to: users-service
  5. Service routes to: users-backend pod
  6. Response: User registration confirmation
```

## DNS Configuration Example

### External DNS Setup
```bash
# DNS A Records
api.mystore.com.     300    IN    A    203.0.113.10
admin.mystore.com.   300    IN    A    203.0.113.10
app.mystore.com.     300    IN    A    203.0.113.10

# Optional CNAME Records
www.mystore.com.     300    IN    CNAME    app.mystore.com.
```

### Internal DNS (CoreDNS)
```bash
# Kubernetes internal DNS
orders-service.ecommerce.svc.cluster.local    → 10.96.100.50
users-service.ecommerce.svc.cluster.local     → 10.96.100.51
admin-service.ecommerce.svc.cluster.local     → 10.96.100.52
```

## Testing the Setup

### 1. Test Path-Based Routing
```bash
# Test orders API
curl -H "Host: api.mystore.com" http://203.0.113.10/orders/123

# Test users API
curl -H "Host: api.mystore.com" http://203.0.113.10/users/profile

# Test different paths
curl -H "Host: api.mystore.com" http://203.0.113.10/orders/search?status=pending
curl -H "Host: api.mystore.com" http://203.0.113.10/users/auth/login
```

### 2. Test Host-Based Routing
```bash
# Test admin panel
curl -H "Host: admin.mystore.com" http://203.0.113.10/

# Test API gateway
curl -H "Host: api.mystore.com" http://203.0.113.10/

# Different hosts, same path
curl -H "Host: admin.mystore.com" http://203.0.113.10/dashboard
curl -H "Host: api.mystore.com" http://203.0.113.10/dashboard  # This would 404
```

### 3. Internal Service Communication
```bash
# From inside a pod
kubectl exec -it orders-backend-pod -- curl users-service.ecommerce.svc.cluster.local/validate
```

This example shows exactly how external DNS requests flow through the Kubernetes routing system and demonstrates the clear difference between path-based and host-based routing!
