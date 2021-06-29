import json
import boto3
import os

fedex_table = os.environ['FEDEX_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(fedex_table)

def getCustomer(event,context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    customer_id=path.split("/")[-1]
    response=table.get_item(
        Key={
            'pk':customer_id,
            'sk':'information'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putCustomer(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    customer_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(customer_id)
    item = {
        'pk': customer_id,
        'sk': 'information',
        'customer_name': body["customer_name"],
        'residence': body["residence"],
        'times_used_service': str(body["times_used_service"]),
        'email':body["email"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def getPackage(event,context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    package_id=path.split("/")[-1]
    response=table.get_item(
        Key={
            'pk':package_id,
            'sk':'information'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putPackage(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    package_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(package_id)
    item = {
        'pk': package_id,
        'sk': 'information',
        'dimentions':str(body["dimentions"]),
        'weigth': str(body["weigth"]),
        'type_package': body["type_package"],
        'distance':str(body["distance"]),
        'origin':body["origin"],
        'destination':body["destination"],
        'estimated_price':str(body["estimated_price"]),
        'discounts':str(body["discounts"]),
        'total_price':str(body["total_price"]),
        'date_registered':body["date_registered"],
        'state':body["state"],
        'state_done':body["state_done"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getCustomerPackageState(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    package_id = path.split("/")[-1] 
    customer_id = path.split("/")[-3] 
    response = table.get_item(
        Key={
            'pk': customer_id,
            'sk': package_id
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def putCustomerAndPackage(event,context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    package_id = path.split("/")[-1] 
    customer_id = path.split("/")[-3] 
    
    body = json.loads(event["body"])
    item = {
        'pk': customer_id,
        'sk': package_id,
        'state': body["state"],
        'state_done': body["state_done"],
        'total_price':str( body["total_price"]),
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Funcion completada con exito!')
    }

    
    
    





