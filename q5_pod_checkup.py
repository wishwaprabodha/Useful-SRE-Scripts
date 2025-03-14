import requests

KUBE_API_URL = "http://127.0.0.1:8001/apis/metrics.k8s.io/v1beta1/pods"
TOKEN_PATH = "/Users/wishwa.wijeratne/SRE/assignment/token"

with open(TOKEN_PATH, "r") as file:
    token = file.read().strip()

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

response = requests.get(KUBE_API_URL, headers=headers, verify=False)

if response.status_code == 200:
    data = response.json()
    for pod in data["items"]:
        print(pod)
        if "spec" not in pod:
            name = pod["metadata"]["name"]
            print(f"Skipping pod {name} (no 'spec' key found)")
            continue

        name = pod["metadata"]["name"]
        namespace = pod["metadata"]["namespace"]
        cpu = pod["containers"][0]["usage"]["cpu"]
        memory = pod["containers"][0]["usage"]["memory"]
        cpu_requests = pod["spec"]["containers"][0].get("resources", {}).get("requests", {}).get("cpu", "N/A")
        memory_requests = pod["spec"]["containers"][0].get("resources", {}).get("requests", {}).get("memory", "N/A")
        if cpu_requests != "N/A" and memory_requests != "N/A":
            memory_value = int(memory[:-2]) * (1024 if memory.endswith("Ki") else 1)
            memory_request_value = int(memory_requests[:-2]) * (1024 if memory_requests.endswith("Ki") else 1)
            cpu_value = int(cpu[:-2]) * (1024 if cpu.endswith("Ki") else 1)
            cpu_request_value = int(cpu_requests[:-2]) * (1024 if cpu_requests.endswith("Ki") else 1)
            cpu_usage = (cpu_value/cpu_request_value) * 100
            memory_usage = (memory_value/memory_request_value) * 100
            if cpu_usage <= 20 or memory_usage <=20:
                print(f"To Optimize - Pod: {name} | Namespace: {namespace} | CPU Usage: {cpu_usage} | Memory Usage: {memory_usage}")
else:
    print(f"Error: {response.status_code} - {response.text}")
