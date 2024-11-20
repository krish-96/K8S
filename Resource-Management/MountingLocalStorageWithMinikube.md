# Adding the local storage to minikube

This is helpful while working with PersistentVolume

Here's the mount command in Markdown format with a brief explanation:

```bash
# Start Minikube with a hostPath mount
minikube start --mount --mount-string="/mnt/data:/mnt/data"
```

Explanation:

- **--mount:** Enables mounting a local directory into the Minikube VM or container.
- **--mount-string:** Specifies the mapping between the local host directory and the path inside Minikube in the format host_path:minikube_path.
- **/mnt/data (Host):** The directory on your local machine that you want to share.
- **/mnt/data (Minikube):** The directory inside Minikube where the host directory will be accessible.

This allows data to be shared between your local machine and the Minikube cluster, which is particularly useful for PersistentVolume setups using hostPath.


---
