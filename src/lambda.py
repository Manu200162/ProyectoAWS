import json
import boto3
import os

database = os.environ["MY_DATABASE"]
language = os.environ["MAIN_LANGUAGE"]
def lambda_handler(event, context):
    #Records[] -> EventName
    for record in event["Records"]:
        if(record["eventName"]=="MODIFY"):
            print("SUCCESS")
        else:
            print("FAIL")
    # TODO implement
    print(json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
