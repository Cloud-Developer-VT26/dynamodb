import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cloud-vt26-book-reviews")

def lambda_handler(event, context):
    # id, name, city
    member = json.loads(event["body"])

    table.put_item( 
        Item={
            "pk": f"MEMBER#{member["id"]}",
            "sk": "PROFILE",
            "name": member["name"],
            "city": member["city"]
        })

    return {
        "statusCode": 200,
        "body": json.dumps({ "success": True, "message": "Member added" })
    }