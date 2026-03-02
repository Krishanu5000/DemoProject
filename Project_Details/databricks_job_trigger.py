"""
S3 Upload
   ↓
S3 Event Notification
   ↓
AWS Lambda
   ↓
Databricks REST API
   ↓
Databricks Workflow / Job
   ↓
Spark ETL Processing
"""

"""
1. File Uploaded to S3
s3://sales-bucket/raw/orders_2026_03_01.csv

2.S3 Event Notification Configured
Event Type: PUT
Trigger: AWS Lambda

3.Lambda Receives Event
{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "sales-bucket"
        },
        "object": {
          "key": "raw/orders_2026_03_01.csv"
        }
      }
    }
  ]
}

4.Lambda Extracts File Info
bucket = event["Records"][0]["s3"]["bucket"]["name"]
key = event["Records"][0]["s3"]["object"]["key"]

print("Bucket:", bucket)
print("File:", key)

5.Lambda Calls Databricks REST API

Lambda triggers a Databricks Job using Jobs API

"""

import json
import requests
import os

DATABRICKS_HOST = os.environ["DATABRICKS_HOST"]
DATABRICKS_TOKEN = os.environ["DATABRICKS_TOKEN"]
JOB_ID = os.environ["JOB_ID"]


def lambda_handler(event, context):
    # Extract S3 details
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    print(f"File uploaded: s3://{bucket}/{key}")

    # Databricks Job API endpoint
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/run-now"

    headers = {
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "job_id": int(JOB_ID),
        "notebook_params": {
            "input_path": f"s3://{bucket}/{key}"
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    print("Databricks response:", response.text)

    return {
        "statusCode": 200,
        "body": "Databricks job triggered"
    }
