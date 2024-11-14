# Kubernetes Rolling Update Deployment Strategy

This document provides a brief explanation of the Kubernetes Rolling Update Deployment Strategy.

In this strategy:

- Kubernetes incrementally updates the application by replacing instances of the old version (v1) with the new version (v2) one or a few at a time.
- During the update, there is no downtime, as some instances of the old version are always running until replaced by new instances.
- Rolling updates are often used for applications where continuous availability is essential, and minimal disruption is allowed.

---

## Workflow

1. Kubernetes begins by updating a subset of the pods to the new version.
2. The update proceeds in batches, maintaining a specific number of old-version pods while bringing up new-version pods.
3. Kubernetes continuously monitors the health of the new pods. If any issues arise, the update can be paused, rolled back, or adjusted as needed.

---

## Important Configuration Options

- **maxUnavailable:** Sets the maximum number of pods that can be unavailable during the update process.
- **maxSurge:** Defines the maximum number of extra pods that can be created above the original number of replicas.

---

## Advantages

- **High Availability:** Minimizes downtime, as the old version is gradually replaced with the new version.
- **Configurable:** Offers control over the update speed and tolerance for pod unavailability.
- **Easy Rollback:** Simplifies reversion to a stable state if issues are detected during the update.

---

## Use Cases

- Ideal for **production environments** requiring continuous service availability.
- Suitable when **minimizing downtime** is a priority and a gradual update process is acceptable.
- Best used when **in-place updates** without noticeable service disruption are required.

---

## Demo

**1. Create an Initial Deployment (v1)**

Create a YAML file my-app-deployment.yaml with the following content for the initial version (v1):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1 # Maximum number of pods that can be unavailable during the update
      maxSurge: 1 # Maximum number of extra pods above the desired count
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app-container
          image: my-app:v2
```

Apply this deployment using:

```bash
kubectl apply -f my-app-deployment.yaml
```

Verify the deployment is running:

```bash
kubectl get deployments
```

**2. Update the Deployment to a New Version (v2)**

Use the kubectl set image command to update the deployment to a new image version (v2):

```bash
kubectl set image deployment/my-app my-app-container=my-app:v2
```

This command will trigger a rolling update where v1 pods are gradually replaced by v2 pods.

**3. Monitor the Rollout Progress**
To monitor the rollout progress and see when the update is complete, use:

```bash
kubectl rollout status deployment/my-app
```

**4. Check the Status of Pods**
Optionally, you can check the individual pods to see how many v1 and v2 instances are running during the update:

```bash
kubectl get pods -l app=my-app -o wide
```

**5. Roll Back if Necessary**
If issues occur during the update, you can roll back to the previous version:

```bash
kubectl rollout undo deployment/my-app
```

Confirm that the rollback has reverted the application to v1 by re-checking the pods and deployment status:

```bash
kubectl get pods -l app=my-app -o wide
kubectl rollout status deployment/my-app
```

---

### Explanation

##### 1. maxUnavailable:

- Specifies the maximum number of pods that can be unavailable during the rolling update process.
- If you set **maxUnavailable**: 1, at most one pod can be taken down before bringing up a new pod.
- This helps ensure there is minimal disruption by keeping most pods running while the update progresses.
- A typical range is from 0 (meaning no pod downtime is allowed) up to 100% of the replicas.

##### 2. maxSurge:

- Specifies the maximum number of additional pods that can be created above the desired replica count during the update.
- For example, **maxSurge**: 1 allows the rolling update to create one extra pod beyond the desired replica count.
- This allows the new version of the pods to start before terminating the old version, enabling a smoother transition.
- A common setting is 25% (meaning up to 25% extra replicas during rollout), but you can also specify absolute numbers.```

##### Typical Use Cases:

**Zero-Downtime Updates:** If you need to maintain full capacity during the update, you can set maxUnavailable: 0 and maxSurge: 1. This will ensure that a new pod is created before an old pod is taken down, effectively maintaining full service during the transition.
**Faster Updates with Minor Downtime:** Setting maxUnavailable: 1 and maxSurge: 2 can speed up the update by allowing some downtime and allowing multiple new pods to come up concurrently.
