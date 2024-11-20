<h1 style="text-align:center;color:green;">Persistent Volume</h>

<h2 style="text-align:center;">Mounting the host data into kubernetes</h2>

Configure a Pod to Use a PersistentVolume for Storage [K8S Doc](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/)

Here’s a concise breakdown of the mounts and their usage:

```text
  I have used /mn/data, /var/log/flask/ here, You can use any path
```

**Persistent Volume (hostPath):** Maps a directory on the Kubernetes node (e.g., /mnt/data) to a Persistent Volume.
Ensures data persists outside the pod's lifecycle.
**_Usage:_** Define in the PersistentVolume spec with hostPath.

**Persistent Volume Claim (PVC):** Requests storage from a Persistent Volume to be used by a pod.
**_Usage:_** Reference the PVC in the Deployment spec under volumes.

**Volume Mount (volumeMounts):** Maps the Persistent Volume (or PVC) to a directory inside the container (e.g.,
/var/log/flask/).
**_Usage:_** Define in the Deployment spec to bind the volume to the desired container path.

**Code Path (log_file_path):** Specifies where the application writes logs (e.g., /var/log/flask/).
**_Usage:_** Align this with the mountPath in the container (e.g., set log_file_path = "/var/log/flask/" if that’s where
the volume is mounted).

1. **Mount the Volume to /var/log/flask/ in the Container**
   Update the volumeMounts section of your deployment to mount the Persistent Volume at /var/log/flask/ inside the
   container:

   deployement.yml

   ```yaml
   volumeMounts:
     - mountPath: "/var/log/flask/"
       name: flask-app-pv-storage
   ```

2. **Ensure the Code Matches the Mount Path**
   Your Python code should use /var/log/flask/:

   ```python
   log_file_path = "/var/log/flask/"
   log_file_abs_path = os.path.join(log_file_path, log_file_name)
   ```

3. **Ensure the Host Path is Set Correctly**
   The hostPath in your Persistent Volume should point to a directory on the host where you want to persist the logs (
   e.g., /mnt/data).

   pv.yml

   ```yaml
   hostPath:
     path: "/mnt/data"
   ```

---

<h2 style="text-align:center;color:darkgreen;">Summary:</h2>

- I have use /mnt/data directory on my hos to store the kubernetes data
- I have mounted /mnt/data directory in kubernetes as /var/log/flask directory.
- In my code I used /var/log/flask directory to store the logs.

---
