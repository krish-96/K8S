# Resource Limits and Requests in Kubernetes

## 1. Resource Requests and Limits for CPU and Memory

### Definitions:

- **Requests**:

  - Minimum resources guaranteed to the container.
  - Used by the Kubernetes scheduler to place pods on nodes with sufficient capacity.

- **Limits**:
  - Maximum resources the container can consume.
  - Containers exceeding the memory limit are terminated; exceeding the CPU limit results in throttling.

### Example:

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "512Mi"
  limits:
    cpu: "1"
    memory: "1024Mi"
```

### Impact on 2 Pod Replicas:

- **Per Pod**:

  - CPU request: `500m`
  - Memory request: `512Mi`
  - CPU limit: `1`
  - Memory limit: `1024Mi`

- **Total (2 replicas)**:
  - Requested CPU: `500m * 2 = 1 CPU`
  - Requested Memory: `512Mi * 2 = 1024Mi`
  - Maximum CPU: `1 * 2 = 2 CPUs`
  - Maximum Memory: `1024Mi * 2 = 2048Mi`

### Key Points:

- Kubernetes guarantees **requests** and enforces **limits**.
- The total requested resources determine node selection for the pods.

## 2. Resource Requests and Limits for Ephemeral Storage

### Definitions:

- **Ephemeral Storage**:
  - Temporary storage on the node used for logs, temp files, and scratch space.
  - Cleared when the pod terminates.

### Example:

```yaml
resources:
  requests:
    ephemeral-storage: "2Gi"
  limits:
    ephemeral-storage: "4Gi"
```

### Impact on 2 Pod Replicas:

- **Per Pod**:

  - Storage request: `2Gi`
  - Storage limit: `4Gi`

- **Total (2 replicas)**:
  - Requested Storage: `2Gi * 2 = 4Gi`
  - Maximum Storage: `4Gi * 2 = 8Gi`

### Behavior:

- **Requests**:

  - Ensures at least `2Gi` of ephemeral storage per pod is available on the node.
  - Pods remain in `Pending` state if the node cannot meet the request.

- **Limits**:
  - Prevents containers from using more than `4Gi` of ephemeral storage.
  - Containers exceeding the limit are terminated.

## 3. Best Practices

### CPU and Memory:

- Use realistic values for **requests** to avoid under/over-utilization of cluster resources.
- Use **limits** to prevent resource contention and protect cluster stability.
- Use monitoring tools to adjust these values based on actual usage.

### Ephemeral Storage:

- Monitor ephemeral storage usage using `kubectl` or other tools.
- Use **Persistent Volumes (PVs)** for long-term storage needs.
- Configure **ResourceQuotas** to manage ephemeral storage usage across namespaces.

### General:

- Ensure cluster nodes have sufficient capacity for the total requested resources.
- Use Horizontal Pod Autoscaler (HPA) for dynamic scaling of replicas.
