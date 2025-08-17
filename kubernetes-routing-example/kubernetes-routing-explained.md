# Kubernetes Routing Explained with Examples

## Overview
Kubernetes routing involves multiple components working together to route traffic from external clients to your applications running in pods.

## Flow of External DNS Request to Pod

```
External Client → DNS → Load Balancer → Ingress Controller → Service → Pod
```

### Step-by-Step Example

1. **External Client Request**: `https://api.mycompany.com/orders`
2. **DNS Resolution**: Domain resolves to Load Balancer IP
3. **Load Balancer**: Routes to Ingress Controller
4. **Ingress Controller**: Applies routing rules
5. **Service**: Distributes to healthy pods
6. **Pod**: Processes the request

## Core Routing Components

### 1. kube-proxy
- **Purpose**: Runs on each node, maintains network rules for service routing
- **Function**: Implements service abstraction by routing traffic to pods
- **Modes**: iptables, IPVS, or userspace proxy modes

### 2. DNS (CoreDNS)
- **Purpose**: Provides service discovery within the cluster
- **Function**: Routes requests like `service-name.namespace.svc.cluster.local`
- **Benefit**: Enables pod-to-service communication by name

### 3. CNI (Container Network Interface)
- **Purpose**: Manages pod networking and IP allocation
- **Function**: Handles pod-to-pod communication across nodes
- **Examples**: Calico, Flannel, Weave Net

## Ingress Routing Types

### Path-Based Routing
Routes traffic based on the URL path to **different services/applications**.

**Example**:
- `api.mycompany.com/orders` → Orders Service
- `api.mycompany.com/users` → Users Service
- `api.mycompany.com/payments` → Payments Service

### Host-Based Routing
Routes traffic based on the hostname/domain to **different services/applications**.

**Example**:
- `orders.mycompany.com` → Orders Service
- `users.mycompany.com` → Users Service
- `payments.mycompany.com` → Payments Service

### Combined Routing
You can combine both approaches:
- `orders.mycompany.com/api` → Orders API
- `orders.mycompany.com/admin` → Orders Admin Panel
- `users.mycompany.com/api` → Users API

## Important Clarification

**Host-based routing is NOT about different deployments of the same app**. It's about routing to completely different services/applications based on the domain name.

If you want different deployments (like staging vs production), you would typically use:
- Different namespaces: `orders-staging` vs `orders-production`
- Different clusters entirely
- Or different ingress rules with different domains: `staging.mycompany.com` vs `mycompany.com`

## Complete Example

Let's see how this works with our e-commerce application:

### External DNS Request Flow

1. **User types**: `https://api.mystore.com/orders/123`
2. **DNS lookup**: `api.mystore.com` → `203.0.113.10` (Load Balancer IP)
3. **Load Balancer**: Forwards to Ingress Controller
4. **Ingress Controller**: 
   - Sees hostname: `api.mystore.com`
   - Sees path: `/orders/123`
   - Matches ingress rule
   - Routes to `orders-service`
5. **Service**: Load balances to one of the `orders-backend` pods
6. **Pod**: Processes the order request

### Ingress Configuration Examples

#### Path-Based Routing
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-ingress
spec:
  rules:
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
      - path: /payments
        pathType: Prefix
        backend:
          service:
            name: payments-service
            port:
              number: 80
```

#### Host-Based Routing
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-host-ingress
spec:
  rules:
  - host: orders.mystore.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: orders-service
            port:
              number: 80
  - host: users.mystore.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: users-service
            port:
              number: 80
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

#### Combined Routing
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: combined-ingress
spec:
  rules:
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
  - host: admin.mystore.com
    http:
      paths:
      - path: /orders
        pathType: Prefix
        backend:
          service:
            name: orders-admin-service
            port:
              number: 80
      - path: /analytics
        pathType: Prefix
        backend:
          service:
            name: analytics-service
            port:
              number: 80
```

## Real-World Scenarios

### Scenario 1: Microservices API Gateway
```
api.company.com/orders → Orders Microservice
api.company.com/inventory → Inventory Microservice
api.company.com/payments → Payments Microservice
api.company.com/notifications → Notifications Microservice
```

### Scenario 2: Multi-Tenant Application
```
tenant1.app.com → Tenant 1's Application Instance
tenant2.app.com → Tenant 2's Application Instance
tenant3.app.com → Tenant 3's Application Instance
```

### Scenario 3: Environment Separation
```
api.company.com → Production API
staging-api.company.com → Staging API
dev-api.company.com → Development API
```

## Network Policies for Security

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: orders-network-policy
spec:
  podSelector:
    matchLabels:
      app: orders-backend
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    - podSelector:
        matchLabels:
          app: api-gateway
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
```

## Summary

- **Path-based routing**: Different URL paths go to different services
- **Host-based routing**: Different domains go to different services
- **kube-proxy**: Handles service-to-pod routing on each node
- **CoreDNS**: Provides internal service discovery
- **CNI**: Manages pod-to-pod networking
- **Ingress Controller**: Routes external traffic to internal services
- **Network Policies**: Control traffic flow for security
