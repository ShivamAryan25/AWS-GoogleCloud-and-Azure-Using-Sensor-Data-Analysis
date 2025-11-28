# AWS-GoogleCloud-and-Azure-Using-Sensor-Data-Analysis

A benchmarking tool to compare serverless function performance across AWS Lambda, Google Cloud Functions, and Azure Functions using temperature sensor data analysis.

## Overview

This project deploys identical temperature analysis functions across three major cloud providers and compares their response latencies. The comparison script sends sensor data to each endpoint and visualizes performance differences.

## Features

- **Multi-cloud deployment**: Same logic deployed to AWS, GCP, and Azure
- **Temperature analysis**: Calculates averages, detects anomalies, and identifies trends
- **Latency benchmarking**: Measures and compares response times across providers
- **Visual comparison**: Generates matplotlib charts for easy analysis

## Project Structure

```
.
├── main.py           # AWS Lambda function (also adaptable for GCP/Azure)
├── comparison.py     # Benchmarking script that tests all three endpoints
└── README.md         # This file
```

## Setup

### Prerequisites

- Python 3.7+
- Required packages: `requests`, `matplotlib`

```bash
pip install requests matplotlib
```

### Cloud Function Deployment

1. **AWS Lambda**: Deploy `main.py` with a Function URL or API Gateway endpoint
2. **Google Cloud Functions**: Adapt the handler and deploy with HTTP trigger
3. **Azure Functions**: Convert to Azure Functions format and deploy with HTTP trigger

### Configuration

Edit `comparison.py` and add your deployed endpoint URLs:

```python
GCP_URL = "https://your-gcp-function-url"
AZURE_URL = "https://your-azure-function-url"
AWS_URL = "https://your-aws-lambda-url"
```

## Usage

Run the comparison test:

```bash
python comparison.py
```

The script will:
1. Generate random temperature sensor data (20-40°C range)
2. Send 10 requests to each cloud provider
3. Measure response latency for each request
4. Display results in terminal
5. Generate a comparison chart

### Sample Output

```
📡 Testing GCP...
GCP Run 1: 145.23 ms   Status: 200
GCP Run 2: 132.45 ms   Status: 200
...

📡 Testing Azure...
Azure Run 1: 178.91 ms   Status: 200
...

📡 Testing AWS...
AWS Run 1: 123.67 ms   Status: 200
...
```

## Temperature Analysis Function

The serverless function analyzes temperature data and returns:

- **average_temperature**: Mean of all readings
- **min_temperature**: Lowest reading
- **max_temperature**: Highest reading
- **anomalies_detected**: Values more than 3° from average
- **trend**: Increasing or decreasing based on last 5 readings
- **processing_time_ms**: Function execution time

### API Request Format

```json
{
  "values": [22.4, 23.1, 21.8, 24.5, 23.0, 22.7, 23.3]
}
```

### API Response Format

```json
{
  "platform": "AWS Lambda",
  "average_temperature": 23.0,
  "min_temperature": 21.8,
  "max_temperature": 24.5,
  "anomalies_detected": [],
  "trend": "increasing",
  "processing_time_ms": 0.234
}
```

## Customization

### Adjust Test Parameters

In `comparison.py`, modify:

```python
TOTAL_RUNS = 10  # Number of test iterations
```

### Adjust Temperature Range

In `comparison.py`, change the sensor data generator:

```python
def generate_sensor_data():
    return {"values": [round(random.uniform(20, 40), 2) for _ in range(7)]}
```

## Results Interpretation

The generated chart shows latency trends across providers. Consider:

- **Cold start impact**: First requests may be slower
- **Geographic proximity**: Distance from your location affects latency
- **Provider infrastructure**: Each cloud has different optimization strategies
- **Network conditions**: Results may vary based on internet connection

## Contributing

Feel free to extend this project by:
- Adding more cloud providers (IBM Cloud, Oracle Cloud, etc.)
- Implementing more complex analysis algorithms
- Adding statistical analysis of results
- Creating automated deployment scripts

## License

MIT License - feel free to use and modify as needed.
