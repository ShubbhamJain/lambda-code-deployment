import json


def lambda_handler(event, context):
    print(json.dumps(event))
    print("Hello from Lambda via docker and ECR!")
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda via docker and ECR!"),
    }
