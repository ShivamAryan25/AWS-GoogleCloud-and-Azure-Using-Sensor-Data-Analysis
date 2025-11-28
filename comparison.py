import requests
import time
import random
import matplotlib.pyplot as plt


GCP_URL = "https://functionn-768541095364.asia-south2.run.app"
AZURE_URL = "https://functionn-btfvecc9dpbhdrh0.centralindia-01.azurewebsites.net/api/HttpTrigger1?code=4ri4Db-6E7u3li4EIULKktu1_0lTSQ82IPzdZ_cN7VZLAzFuJXji9Q=="
AWS_URL = "https://r4rpjimdch.execute-api.us-east-1.amazonaws.com/default/fog_pbl"   

TOTAL_RUNS = 10



def generate_sensor_data():
    
    return {"values": [round(random.uniform(20, 40), 2) for _ in range(7)]}



def test_endpoint(name, url):
    latencies = []

    print(f"\n📡 Testing {name}...")

    for i in range(TOTAL_RUNS):
        data = generate_sensor_data()
        start = time.time()

        try:
            response = requests.post(url, json=data)
            elapsed = (time.time() - start) * 1000  
            latencies.append(elapsed)
            print(f"{name} Run {i+1}: {elapsed:.2f} ms   Status: {response.status_code}")

        except Exception as e:
            print(f"Error calling {name}: {e}")
            latencies.append(None)

    return latencies



gcp_lat = test_endpoint("GCP", GCP_URL)
azure_lat = test_endpoint("Azure", AZURE_URL)
aws_lat = test_endpoint("AWS", AWS_URL)


plt.figure(figsize=(12, 6))
plt.plot(gcp_lat, marker="o", label="GCP Latency (ms)")
plt.plot(azure_lat, marker="o", label="Azure Latency (ms)")
plt.plot(aws_lat, marker="o", label="AWS Latency (ms)")

plt.title("GCP vs Azure vs AWS — Latency Comparison")
plt.xlabel("Test Number")
plt.ylabel("Latency (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
