import json
import requests


def lambda_handler(event, context):
    path = event.get('path')

    if path == "/hello" or path == "/hello/":
        message = hello()
    elif path == "/hi" or path == "/hi/":
        message = hi()

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            # "location": ip.text.replace("\n", "")
        }),
    }


def hello():
    return "Hello from hello function"


def hi():
    return "Hi from hi function"
