# Ku­ber­netes Re­source Op­ti­miza­tion

This Python script retrieves CPU and memory usage metrics for pods in a Kubernetes cluster using the Metrics API. It identifies pods with CPU or memory usage at or below 20% of their requested resources, suggesting potential optimization opportunities.

## Features

- **Fetch Pod Metrics:**
  Connects to the Kubernetes Metrics API to retrieve real-time CPU and memory usage for each pod.

- **Resource Utilization Analysis:**
  Compares actual usage against requested resources to calculate utilization percentages.

- **Optimization Suggestions:**
  Identifies pods with CPU or memory usage at or below 20% of their requested resources, indicating potential over-allocation.

## Prerequisites

- **Kubernetes Cluster:**
  Ensure you have access to a running Kubernetes cluster with the Metrics Server installed. The Metrics Server is essential for collecting resource metrics and is not deployed by default. For installation instructions, refer to the [Kubernetes documentation][metrics-server-setup].

- **Authentication Token:**
  Obtain a valid Kubernetes API access token. This token is used to authenticate API requests and should have sufficient permissions to access pod metrics.

- **Python Environment:**
  - Python 3.x
  - `requests` library (install via `pip install requests`)

## Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/k8s-pod-resource-monitor.git
   cd k8s-pod-resource-monitor

## Testing Concerns

1. **Tested locally with minikube using kube proxy**
2. **Ideally SA Token should be red from dir where k8s SA secret is stored and decoding the base64 encoding string.**
3. **For this I have used the below command to get the auth token and saved it to a file**
```
kubectl get secret metrics-reader-token -o jsonpath='{.data.token}' -n default | base64 --decode
```
4. **For reference I have commited secret, serviceAccount, role and roleBinding declarations too.**
