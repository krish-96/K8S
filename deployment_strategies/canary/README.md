# Canary Deployment Strategy

In this deployment strategy:

- We create a new version (v2) with the same number of replicas as the existing version (v1).

- The same Ingress controller used for v1 will route traffic to v2 for testing.

- If v2 is stable, we can delete the replicas of v1.

- If v2 encounters issues, we can route all traffic back to v1 without causing any disruption.

## Demo

**1. Search for the following term online:**

```text
nginx canary kubernetes
```

**2. Click on GitHub page**
Once you find the Canary setup documentation page, proceed with the steps listed there.

[Canary Setup Documentation](https://kubernetes.github.io/ingress-nginx/examples/canary/)

**3. Testing the canary deployment strategy**
After creating the deployment, service, and ingress for the main and canary services, as described in the documentation, use the following command to test the setup:

```bash
for i in $(seq 1 10); do curl -s --resolve echo.prod.mydomain.com:80:$INGRESS_CONTROLLER_IP echo.prod.mydomain.com  | grep "Hostname"; done
```

To obtain INGRESS_CONTROLLER_IP, run the command below:

```bash
$ kubectl get ing
NAME         CLASS   HOSTS                    ADDRESS        PORTS   AGE
production   nginx   echo.prod.mydomain.com   192.168.58.2   80      73s
```

If you are using this setup locally, retrieve the IP with:

```bash
$ minikube ip
192.168.58.2
```

## Advantages:

- We can control the traffic based on the required.
- Since we can reduce the traffic, number of users affected will be less.
- Best suitable for production testing.
- Very powerfulwhen compared to Rolling update.
- We can gradually increase the traffic, if something goes wrong we can switch all the traffic to existing version.

## Applications

- This strategy is best suitable when we don't have downtime
- Testing in Production environment

### $Note:$

> If there's possibility for the Downtime and the required downtime doesn't impact the use traffic and experience, then we can go with Rolling update strategy.
> When there's no way to get the downtime, then will go with Canary deployment starategy.
