import json

def lambda_handler(event, context):
    for record in event['Records']:
       print ("Lambda")
       payload=record["body"]
       print(str(payload))
