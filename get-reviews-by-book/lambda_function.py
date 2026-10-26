import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cloud-vt26-book-reviews")

def lambda_handler(event, context):
    # isbn som queryparamter
    isbn = event["queryStringParameters"]["isbn"]

    print(json.dumps(event))

    response = table.query(
        KeyConditionExpression="pk = :pk AND begins_with(sk, :sk)",
        ExpressionAttributeValues={
            ":pk": f"BOOK#{isbn}",
            ":sk": "REVIEW#"
        }
    )

    print(json.dumps(response))

    return {
        "statusCode": 200,
        "body": json.dumps({ "success": True, "reviews": response["Items"] })
    }