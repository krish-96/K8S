<h3 style="text-align:center;">K8S Components Description / Purpose in 1 line</h3>

<hr>
Here’s a one-liner for each Kubernetes component:

<h4>Cluster Nodes</h4>

1. **Master Node (Control Plane):** Manages the cluster, handling deployments, resource allocation, and scaling.
2. **Worker Node:** Runs your applications in containers within Pods.

---

<h4 style="text-align:center;text-decoration:underline;">Worker Node Components</h4>

<!-- ## **Worker Node Components** -->

- **Pods:** Smallest deployable units, containing one or more containers that share resources.
- **Kubelet:** An agent that ensures specified containers are running within Pods.
- **CRI (Container Runtime Interface):** Manages container lifecycle with runtimes like Docker or containerd.
- **Kube-Proxy:** Manages Pod network connectivity, load balancing, and service proxies.

### Purpose of the Master Node:
- Manages cluster-wide operations and maintains the desired state.
- Schedules and assigns workloads to worker nodes.
- Ensures resources are efficiently distributed across nodes.

### Purpose of the Worker Node:
- Runs application workloads (pods).
- Provides resources (CPU, memory) to containers.
- Manages networking to support inter-pod communication.

---

<h4 style="text-align:center;text-decoration:underline;">Master Node Components</h4>
<!-- ## **Master Node Components** -->

- **API Server:** Acts as the gateway for all cluster operations, enforcing policies and handling requests.
- **Scheduler:** Selects suitable nodes for Pods based on resource availability and rules.
- **Controller Manager:** Maintains the desired cluster state by monitoring and managing resources.
- **etcd:** A distributed key-value store holding the cluster’s state, accessed by the API Server.

---

## AddOns

- **AddOns:** Extensions for monitoring, logging, networking, and other enhancements (e.g., Helm, CoreDNS).

---

