import json
import decimalencoder
import todoList


def get(event, context):
    # create a response depends on if id is on table or not. If id is not found, we returns error 404
    item = todoList.get_item(event['pathParameters']['id'])
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
