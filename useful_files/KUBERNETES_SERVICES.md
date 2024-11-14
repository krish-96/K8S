# <div  style="color:white;align:center;">Brief explanation for Kubernetes service types</div>

<a id="top"></a>

### Kubernetes Service Types

#### 1. **ClusterIP (Default)**

- **Purpose**: Exposes the service on a cluster-internal IP. This means the service is only accessible from within the
  cluster.
- **Use case**: Best suited for internal communication between pods.

#### 2. **NodePort**

- **Purpose**: Exposes the service on a static port across all nodes in the cluster. External traffic can access the
  service using `NodeIP:NodePort`.
- **Key Features**:
    - **Load Balancing**: Distributes traffic across pods.
    - **Service Discovery**: Manages routing to the appropriate pod.
    - **Expose to the World**: Accessible from outside the cluster.

#### 3. **LoadBalancer**

- **Purpose**: Creates an external load balancer (usually cloud-provided) to route traffic to your service. This is the
  most common choice for production environments.
- **Key Features**:
    - **External Access**: Exposes the service via an external IP.
    - **Auto Scaling**: Integrates with cloud load balancing, ensuring high availability.
- **Use case**: For exposing applications to the internet with automated load balancing.

---

## <span style="color:orange;">Summary</span>

- **ClusterIP**: Internal service, only accessible within the cluster.
- **NodePort**: Exposes service on a static port on all nodes, accessible externally.
- **LoadBalancer**: External access with automatic load balancing, typically for production.
- **ExternalName**: For mapping to external resources, without exposing pods.

---

### Examples:

- ClusterIP YAML (Default service type):

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: flask-service
    spec:
      selector:
        app: flask-app
      ports:
        - protocol: TCP
          port: 80        # Port exposed inside the cluster
          targetPort: 5000 # Port where the Flask app is running inside the pod
      type: ClusterIP     # Default service type
    ```

- NodePort YAML:

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: flask-service
    spec:
      selector:
        app: flask-app
      ports:
        - protocol: TCP
          port: 80
          targetPort: 5000
          nodePort: 30001
      type: NodePort
    ```

- LoadBalancer YAML:

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: flask-service
    spec:
      selector:
        app: flask-app
      ports:
        - protocol: TCP
          port: 80
          targetPort: 5000
      type: LoadBalancer
    ```


```bash
kubectl logs ingress-nginx-controller-bc57996ff-psw29 -n ingress-nginx
minikube kubectl -- get all --watch

```

alias kubectl="minikube kubectl --"



<div style="text-align: right; position: fixed; bottom: 20px; right: 20px;font-size:15px;"><a href="#top">Go2Top</a></div>