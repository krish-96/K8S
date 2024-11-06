<h1 align="center">minikube Commands</h1>

### Starting and Stopping Minikube

- Start Minikube:
  ```bash
  minikube start
  ```
- Stop Minikube:
  ```bash
  minikube stop
  ```

### Cluster Information

- Get Minikube status:
  ```bash
  minikube status
  ```

### Kubernetes Dashboard

- Open the Minikube dashboard:
  ```bash
  minikube dashboard
  ```

### NodePort Access

- Access a service through a NodePort:
  ```bash
  minikube service <service-name> --url
  ```

### Minikube Tunnel

- Start a Minikube tunnel (for accessing NodePort services from the host):
  ```bash
  minikube tunnel
  ```

### Kubernetes Context

- Set Minikube as the Kubernetes context:
  ```bash
  kubectl config use-context minikube
  ```

### SSH Access

- SSH into the Minikube VM:
  ```bash
  minikube ssh
  ```

---
For more about minikube basic control please refer to
[BasiControls](https://minikube.sigs.k8s.io/docs/handbook/controls/)
---

## Notes

- Replace `<service-name>` with the actual name in your Kubernetes setup.
