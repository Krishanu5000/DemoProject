"""EventBridge (schedule)
↓
Step Function
↓
Lambda (check file)
↓
Choice State
↓
SNS
↓
SQS
↓
Lambda
↓
Your S3"""