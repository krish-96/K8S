# Flask Kubernetes Tutorial

received and displays them on a webpage. It is a part of the tutorial where you can practice deploying Flask
applications to Kubernetes clusters.

## Project Overview

The Flask application contains two main routes:

1. **/ (Welcome Page)**:
    - This route logs each request received and displays a count of how many requests have been made. The page also
      provides a brief welcome message styled with HTML and CSS.

2. **/req_count (Request Count)**:
    - This route displays the current number of requests the application has received. It's a simple counter that helps
      track the traffic to the app.

Both routes incorporate logging for tracking requests, responses, and the current state of the application.

## Kubernetes Deployment
``
The project is designed to be deployed on Kubernetes. It includes the following YAML files for setting up the Kubernetes
environment:

- **[Pod Manifest](flask_pod.yaml)**: Defines a single pod to run the Flask application. 
- **[Deployment Manifest](flask_deploy.yaml)**: Configures the deployment for managing replicas and maintaining the Flask application in a
  running state.
- **[Service Manifest](flask_service_node_port.yaml)**: Exposes the Flask application via a `NodePort` service to allow access from outside the
  Kubernetes cluster.

### Kubernetes Setup Instructions

1. Clone the repository to your local machine.
2. Build and push the Docker image for the Flask application to a container registry (e.g., Docker Hub).
3. Apply the Kubernetes manifests using `kubectl`:
   ```bash
   kubectl apply -f pod.yaml
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

To know more about 
- [kubectl commands](useful_files/KUBECTL_COMMANDS.md)
- [minikube commands](useful_files/MINIKUBE_COMMANDS.md)
- [docker commands](useful_files/DOCKER_COMMANDS.md)
- [kubernetes service types](useful_files/SERVICES.md)
