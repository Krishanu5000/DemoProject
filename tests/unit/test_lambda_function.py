import json
from Project_Details.aws_lambda_sample import lambda_handler


class MockContext:
    def __init__(self):
        self.function_name = "test-function"
        self.aws_request_id = "test-request-id"

    def get_remaining_time_in_millis(self):
        return 300000


# ---- Test Case ----
def test_lambda_handler_success():
    # Mock SNS event
    test_event = {
        "Records": [
            {
                "Sns": {
                    "Message": json.dumps({
                        "order_id": 101,
                        "customer": "Krishanu",
                        "amount": 2500
                    })
                }
            }
        ]
    }

    # Create mock context
    context = MockContext()

    # Call Lambda function
    response = lambda_handler(test_event, context)
    # Assertions
    assert response["statusCode"] == 200
    assert response["body"] == "Order processed successfully"
