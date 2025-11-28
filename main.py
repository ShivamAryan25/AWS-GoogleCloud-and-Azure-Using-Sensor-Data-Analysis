import json
import time

def analyze_temperatures(values):
    start = time.time()

    temps = [float(x) for x in values]
    avg_temp = round(sum(temps) / len(temps), 2)
    minimum = min(temps)
    maximum = max(temps)
    anomalies = [t for t in temps if abs(t - avg_temp) > 3]

    if len(temps) >= 5:
        trend = "increasing" if temps[-1] > temps[-5] else "decreasing"
    else:
        trend = "not enough data"

    processing_time_ms = round((time.time() - start) * 1000, 3)

    return {
        "platform": "AWS Lambda",
        "average_temperature": avg_temp,
        "min_temperature": minimum,
        "max_temperature": maximum,
        "anomalies_detected": anomalies,
        "trend": trend,
        "processing_time_ms": processing_time_ms
    }


def lambda_handler(event, context):
    """
    Accepts JSON body like: { "values": [22.4, 23.1, ...] }
    Works with Lambda Function URLs (event will contain 'body' string)
    and API Gateway proxy (same structure).
    """
    
    body = None

    if isinstance(event, dict) and "body" in event and event["body"] is not None:
       
        try:
            body = json.loads(event["body"])
        except Exception:
           
            try:
                body = event["body"]
            except Exception:
                body = None
    else:
       
        body = event if isinstance(event, dict) else None

    if not body:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Send JSON with 'values': [...]"})
        }

    values = body.get("values", [])
    if not values:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Temperature list is empty"})
        }

    result = analyze_temperatures(values)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(result)
    }
