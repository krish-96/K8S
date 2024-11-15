<h2 style="text-align:center;text-decoration:underline;color:green;">Resource Management for Pods and Containers
</h2>

To check more info about this please use the below terms on the browser and open the official Kubernetes link

```test
kubernetes resourcelimit for pod
```

Follow the [document](kubernetes.io/docs/concepts/configuration/manage-resources-containers/) with the detailed steps in

#### Resource Management for Pods and Containers

When you specify the resource request for containers in a Pod, the kube-scheduler uses this information to decide which node to place the Pod on. When you specify a resource limit for a container, the kubelet enforces those limits so that the running container is not allowed to use more of that resource than the limit you set. The kubelet also reserves at least the request amount of that system resource specifically for that container to use.

Resource requests and limits of Pod and container
For each container, you can specify resource limits and requests, including the following:

spec.containers[].resources.limits.cpu
spec.containers[].resources.limits.memory
spec.containers[].resources.limits.hugepages-<size>
spec.containers[].resources.requests.cpu
spec.containers[].resources.requests.memory
spec.containers[].resources.requests.hugepages-<size>

For Demo:

Follow the page to bottom, we can see few examples
