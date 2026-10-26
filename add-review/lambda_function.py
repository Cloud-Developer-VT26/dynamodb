import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cloud-vt26-book-reviews")

def lambda_handler(event, context):
    # isbn, memberId, rating, text
    review = json.loads(event["body"])

    table.put_item( 
        Item={
            "pk": f"BOOK#{review["isbn"]}",
            "sk": f"REVIEW#MEMBER#{review["memberId"]}",
            "rating": review["rating"],
            "text": review["text"]
        })

    table.put_item( 
        Item={
            "pk": f"MEMBER#{review["memberId"]}",
            "sk": f"REVIEW#BOOK#{review["isbn"]}",
            "rating": review["rating"],
            "text": review["text"]
        })

    return {
        "statusCode": 200,
        "body": json.dumps({ "success": True, "message": "Review added" })
    }