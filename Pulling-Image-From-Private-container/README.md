# Pull an Image from a Private Registry

Go to browser and search for "Pull an Image from a Private Registry" and open official K8s link.

And follow the steps.

In the simple context, Will be secreting a secret in K8's for the docker registry where

## Create a Secret by providing credentials on the command line

Create this Secret, naming it regcred: # You can give your own name

```bash
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
```

where:

- <your-registry-server> is your Private Docker Registry FQDN. Use https://index.docker.io/v1/ for DockerHub.
- <your-name> is your Docker username.
- <your-pword> is your Docker password.
- <your-email> is your Docker email

You have successfully set your Docker credentials in the cluster as a Secret called regcred # regcred will be used in
yaml manifest


---
    Note:
    Typing secrets on the command line may store them in your shell history unprotected, and those secrets might also be
    visible to other users on your PC during the time that kubectl is running.
---


## Create a Pod that uses your Secret 

pods/private-reg-pod.yaml 

```json
apiVersion: v1
kind: Pod
metadata:
  name: private-reg
spec:
  containers:
  - name: private-reg-container
    image: <your-private-image>
  imagePullSecrets:
  - name: regcred

```
Here **regcred** is the secret name we just created


If you're using AWS, registry-server will be ECR. You can get this from AWS Documentation

```bash
aws_account_id.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest
```