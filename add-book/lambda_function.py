import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cloud-vt26-book-reviews")

def lambda_handler(event, context):
    # isbn, title, author
    book = json.loads(event["body"])

    table.put_item( 
        Item={
            "pk": f"BOOK#{book["isbn"]}",
            "sk": "PROFILE",
            "title": book["title"],
            "author": book["author"]
        })

    return {
        "statusCode": 200,
        "body": json.dumps({ "success": True, "message": "Book added" })
    }