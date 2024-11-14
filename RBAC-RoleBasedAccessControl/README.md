# RBAC-RoleBasedAccessControl
1. kubectl create serviceaccount restricted-user -n default

In Kubernetes, you typically authenticate users using certificates or external identity providers rather than creating users directly within the cluster. However, you can create service accounts or use a simple certificate-based approach to simulate user access control. Here’s how to create a new "user" with restricted permissions in Minikube:

Step 1: Create a Service Account
Service accounts are often used for applications but can also act as users with restricted permissions.

bash
Copy code
kubectl create serviceaccount restricted-user -n default
This creates a service account called restricted-user in the default namespace.

Step 2: Bind the Service Account to the Role
Next, bind the service account to a restricted role to limit what it can access. You can use the role we created previously (pod-viewer).

yaml
Copy code
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: restricted-user-binding
  namespace: default
subjects:
  - kind: ServiceAccount
    name: restricted-user
    namespace: default
roleRef:
  kind: Role
  name: pod-viewer
  apiGroup: rbac.authorization.k8s.io
Save this to a file (e.g., restricted-role-binding.yaml) and apply it:

bash
Copy code
kubectl apply -f restricted-role-binding.yaml
This binds the pod-viewer role to the restricted-user service account, allowing it to view pods but not secrets.

Step 3: Access the Cluster Using the Service Account
You’ll need to retrieve the service account’s token to use it as an authentication method.

Retrieve the token:

bash
Copy code
SECRET_NAME=$(kubectl get sa restricted-user -o jsonpath='{.secrets[0].name}' -n default)
kubectl get secret $SECRET_NAME -o jsonpath='{.data.token}' -n default | base64 --decode
Configure kubectl to use this token, or set up a new kubeconfig file specifically for this service account if you want to switch contexts easily.

bash
Copy code
kubectl config set-credentials restricted-user --token=<your-token-here>
kubectl config set-context restricted-user-context --cluster=minikube --namespace=default --user=restricted-user
kubectl config use-context restricted-user-context
Now, when you run kubectl commands in the restricted-user-context, you’ll be restricted by the permissions set in the pod-viewer role (e.g., unable to list or access secrets).

Step 4: Testing the Access Control
To test this:

Try listing pods (should succeed):

bash
Copy code
kubectl get pods
Try accessing secrets (should fail):

bash
Copy code
kubectl get secrets
This approach gives you control over access without needing real user accounts and leverages Kubernetes' RBAC model to restrict permissions.









