<h3 style="text-align:center;">K8's Infrastructure</h3>

# K8's Infrastructure

Hierarchical visualization to understand the structure of single-cluster and multi-cluster setups in Kubernetes:

```scss
Kubernetes Infrastructure
│
├── Single Cluster Setup
│   ├── Control Plane (manages the entire cluster)
│   │   ├── API Server
│   │   ├── Scheduler
│   │   ├── Controller Manager
│   │   └── etcd (key-value store)
│   │
│   └── Nodes (Worker Machines)
│       ├── Node 1
│       │   ├── Kubelet
│       │   ├── Kube-proxy
│       │   └── Container Runtime
│       │       ├── Pod A (application container 1)
│       │       └── Pod B (application container 2)
│       │
│       ├── Node 2
│       │   ├── Kubelet
│       │   ├── Kube-proxy
│       │   └── Container Runtime
│       │       ├── Pod C (application container 3)
│       │       └── Pod D (application container 4)
│       │
│       └── Node N
│           ├── Kubelet
│           ├── Kube-proxy
│           └── Container Runtime
│               └── Pods (application containers)
│
└── Multi-Cluster Setup
    ├── Cluster 1 (Region A)
    │   ├── Control Plane
    │   │   ├── API Server
    │   │   ├── Scheduler
    │   │   ├── Controller Manager
    │   │   └── etcd
    │   │
    │   └── Nodes
    │       ├── Node 1 (Region A)
    │       ├── Node 2 (Region A)
    │       └── Node N (Region A)
    │
    ├── Cluster 2 (Region B)
    │   ├── Control Plane
    │   │   ├── API Server
    │   │   ├── Scheduler
    │   │   ├── Controller Manager
    │   │   └── etcd
    │   │
    │   └── Nodes
    │       ├── Node 1 (Region B)
    │       ├── Node 2 (Region B)
    │       └── Node N (Region B)
    │
    └── Cluster Management Tools (optional)
        ├── Kubernetes Federation (manages clusters as a single unit)
        ├── Service Mesh (Istio, Linkerd for cross-cluster communication)
        └── Cluster Registry (e.g., Rancher, Anthos for monitoring and coordination)
```
