## B&G ( Blue & Green) Deployment Strategy

### Introduction

In this type of deployment strategy, Will create v2 with the same number of replicas exists in v1. Same ingress controller which is created for v1 will be used to routes the traffic to version v2.

- If the v2 is working fine then will delete the replicas of version v1
- If the v2 is not working fine then will route all the traffic to version v1 by changing the service name without disturbing the traffic

Why it was named as Blue and Green deployment is it has 2 sights
One is Blue and One is Green

```text
            Blue Sight           |         Green Sight
                  V1             |            V2
            R1  R2  R3  R4       |      R1  R2  R3  R4
                  S1             |            S2
                            LB from IC
                        V1, V2 - Versions
                            R1, R2, R3, R4 - Replicas
                            S1, S2 - Services
                            LB - LoadBalancer
                            IC - IngressController

    Initially LB is refering to S1 i.e., app running version V1
    To servce V2, LB will be refered to S2 i.e., app running version V2
```

## Advantages:

- This is very costly, Because we are creating the same number of replicas. Will not be deleting the replicas on the same day, some time it may requires 1 week also.
- Even though these services in blue sight are not receiving the requests, still consumes the cpi, memory and storage.

## Dis-Advantages:

- This is very safe, Because we are having the existing version safely.
