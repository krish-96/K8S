<h2 style="text-align:center;text-decoration:underline;color:green;">Configure Memory and CPU Quotas for a Namespace
</h2>

To check more info about this please use the below terms on the browser and open the official Kubernetes link

```test
kubernetes resourcelimit for namespace
```

Follow the [document](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/) with the detailed steps in

#### Configure Memory and CPU Quotas for a Namespace

Define overall memory and CPU resource limits for a namespace.

For Demo:

Create a namespace, ResourceQuota and create Pods beyond the resource limit to verify whether ift's allowing or not.

If you try to create a resource which use the CPU and Memory beyond the specified value:

```bash
╭─krishna@cloudking in ~/Desktop/K8S/Resource-Management/Resource Quotas for a Namespace on feature/Metrics ✘
╰$ kubectl apply -f Pod2.yml
Error from server (Forbidden): error when creating "Pod2.yml": pods "quota-mem-cpu-demo-2" is forbidden: exceeded quota: mem-cpu-demo, requested: limits.cpu=800m,limits.memory=1Gi,requests.cpu=400m,requests.memory=700Mi, used: limits.cpu=1800m,limits.memory=1056Mi,requests.cpu=900m,requests.memory=728Mi, limited: limits.cpu=2,limits.memory=2Gi,requests.cpu=1,requests.memory=1Gi
```

**_Note:_** In your case values may differ, because it'll display based on the configured limit
