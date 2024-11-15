<h1 style="text-align:center;text-decoration:underline;color:blue;">K8S Resource Management </h1>

---

<h2 style="text-align:center;text-decoration:underline;color:green;">What & Why Resource management?</h2>

Kubernetes resource management ensures applications use cluster resources efficiently by allowing you to configure requests (guaranteed minimum resources for pods), limits (maximum resource usage), and enabling advanced features like resource quotas (namespace-level limits), autoscaling (horizontal and vertical scaling), and priority classes (scheduling preferences) to balance workloads, prevent overconsumption, and maintain cluster stability.

---

<h2 style="text-align:center;text-decoration:underline;color:green;">K8S Resource Management Units</h2>

Here are the possible units for CPU and Memory in Kubernetes:

<h3 style="text-align:center;text-decoration:underline;">CPU Units</h3>

CPU usage is measured in cores or fractions of cores:

##### Cores:

- Represented as whole numbers (e.g., 1, 2 for 1 or 2 cores).
- Example: 2 means 2 full CPU cores.

##### Millicores (m):

- 1 core = 1000 millicores.
- Example: 500m means 0.5 cores (half a core).

##### Key points:

- Fractions of a core are always represented in m (millicores).
- Kubernetes requests and limits must always be specified as whole numbers (e.g., 250m, 2).

---

<h3 style="text-align:center;text-decoration:underline;">Memory Units</h3>

Memory is measured in bytes with suffixes for larger units. Kubernetes supports these standard units:

##### Binary (Power of 2 - IEC Standard):

- Ki = kibibytes (1024 bytes)
- Mi = mebibytes (1024 KiB)
- Gi = gibibytes (1024 MiB)
- Ti = tebibytes (1024 GiB)
- Pi = pebibytes (1024 TiB)
- Ei = exbibytes (1024 PiB)

##### Decimal (Power of 10 - SI Standard):

- K = kilobytes (1000 bytes)
- M = megabytes (1000 KB)
- G = gigabytes (1000 MB)
- T = terabytes (1000 GB)
- P = petabytes (1000 TB)
- E = exabytes (1000 PB)

---

<h3 style="text-align:center;text-decoration:underline;">Examples</h3>

**CPU:**

- 250m → 0.25 cores.
- 1 → 1 core.
- 2 → 2 cores.

**Memory:**

- 512Mi → 512 mebibytes (binary).
- 1Gi → 1 gibibyte (binary).
- 500M → 500 megabytes (decimal).
- 1G → 1 gigabyte (decimal).

---

<h3 style="text-align:center;text-decoration:underline;">Key Notes</h3>

**CPU:** Only supports cores and millicores (no other units).
**Memory:** Can use either binary (Mi, Gi) or decimal (M, G) units, depending on preference.

---

<h3 style="text-align:center;text-decoration:underline;">Sample Manifest File</h3>

Here's the manifest file with resources configured to create a pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-demo
spec:
  containers:
    - name: demo-container
      image: nginx
      resources:
        requests: # Minimum resources guaranteed
          memory: "128Mi" # 128 MiB of memory
          cpu: "250m" # 0.25 CPU (250 millicores)
        limits: # Maximum resources allowed
          memory: "256Mi" # 256 MiB of memory
          cpu: "500m" # 0.5 CPU (500 millicores)
```

---
