"""File Uploaded to S3
        ↓
S3 publishes event
        ↓
SNS Topic
        ↓
Lambda triggered
        ↓
Databricks Job Starts"""

"""Manual Publisher (CLI/User)
A developer can also publish manually:

aws sns publish \
  --topic-arn arn:aws:sns:region:id:topic \
  --message "Test message"
  
"""

"""
SNS Topic → Subscription → AWS Lambda
"""

"""
Publisher Sends Message to SNS
{
  "order_id": 101,
  "customer": "Krishanu",
  "amount": 2500
}
"""

"""
SNS Triggers Lambda Automatically

SNS pushes the message to Lambda.

Lambda is invoked immediately.

No polling needed
"""

"""
How Lambda Receives the Message

{
  "Records": [
    {
      "Sns": {
        "Message": "{\"order_id\":101,\"customer\":\"Krishanu\",\"amount\":2500}"
      }
    }
  ]
}

SNS message is inside:
event["Records"][0]["Sns"]["Message"]
"""

# Example: Lambda Processing SNS Message (Python)
import json


def lambda_handler(event, context):
    # Extract SNS message
    message = event["Records"][0]["Sns"]["Message"]

    # Convert string to dictionary
    order_data = json.loads(message)

    print("Order ID:", order_data["order_id"])
    print("Customer:", order_data["customer"])
    print("Amount:", order_data["amount"])

    return {
        "statusCode": 200,
        "body": "Order processed successfully"
    }


