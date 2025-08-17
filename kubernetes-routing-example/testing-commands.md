# Kubernetes Routing Testing Commands

# Check all resources in the namespace
kubectl get all -n myapp

# Check ingress details
kubectl describe ingress myapp-ingress -n myapp

# Test service discovery (from inside a pod)
kubectl exec -it deployment/frontend-app -n myapp -- nslookup backend-service
kubectl exec -it deployment/backend-api -n myapp -- nslookup postgres-service

# Check endpoints (actual pod IPs behind services)
kubectl get endpoints -n myapp

# Test internal connectivity
kubectl exec -it deployment/frontend-app -n myapp -- wget -qO- http://backend-service/
kubectl exec -it deployment/backend-api -n myapp -- nc -zv postgres-service 5432

# Monitor traffic (if using nginx ingress)
kubectl logs -f deployment/nginx-ingress-controller -n ingress-nginx

# Check network policies
kubectl get networkpolicies -n myapp
kubectl describe networkpolicy frontend-to-backend -n myapp

# Port forwarding for local testing
kubectl port-forward service/frontend-service 8080:80 -n myapp
# Then access: http://localhost:8080

# Check pod logs
kubectl logs -f deployment/frontend-app -n myapp
kubectl logs -f deployment/backend-api -n myapp
kubectl logs -f deployment/postgres-db -n myapp

# Test load balancing (multiple requests to see different pods)
for i in {1..10}; do
  kubectl exec deployment/frontend-app -n myapp -- wget -qO- http://backend-service/ | grep hostname
done

# Check service endpoints are healthy
kubectl get endpoints backend-service -n myapp -o yaml

# Test ingress routing
curl -H "Host: myapp.local" http://localhost/
curl -H "Host: myapp.local" http://localhost/api/

# Check kube-proxy rules (on nodes)
sudo iptables -t nat -L | grep backend-service
