# <div style="text-align:center;color:green;">kubectl Commands</div>

### Cluster Information

- Get cluster information:
  ```bash
  kubectl cluster-info
  ```
- Get all nodes in the cluster:
  ```bash
  kubectl get nodes
  ```

### Pod Management

- List all pods in a namespace:
  ```bash
  kubectl get pods -n <namespace>
  ```
- Get detailed information about a pod:
  ```bash
  kubectl describe pod <pod-name> -n <namespace>
  ```
- Delete a pod:
  ```bash
  kubectl delete pod <pod-name> -n <namespace>
  ```

### Deployment Management

- List all deployments:
  ```bash
  kubectl get deployments
  ```
- Create a deployment from a YAML file:
  ```bash
  kubectl apply -f <deployment-file>.yaml
  ```
- Delete a deployment:
  ```bash
  kubectl delete deployment <deployment-name>
  ```

### Logs and Monitoring

- Get logs from a pod:
  ```bash
  kubectl logs <pod-name> -n <namespace>
  ```

### Service Management

- List all services:
  ```bash
  kubectl get svc
  ```
- Get details about a service:
  ```bash
  kubectl describe svc <service-name>
  ```

### Namespace Management

- List all namespaces:
  ```bash
  kubectl get namespaces
  ```

### BulkDelete

- To delete all the pods:
  ```bash
  kubectl delete pods --all
  ```
- To delete all the deployments:
  ```bash
  kubectl delete deploy --all
  ```

---
For more about kubernetes commands please refer to the
[CheetSheet](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
---

## Notes

- Replace `<namespace>`, `<pod-name>`, `<service-name>`, and `<deployment-name>` with the actual names in your
  Kubernetes setup.
- Ensure that Minikube is properly configured to interact with Kubernetes when using `kubectl`.
- If we didn't provide namespace, default namespace will be used
