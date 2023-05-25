import json
import logging
import decimalencoder
import todoList


def update(event, context):
    data = json.loads(event['body'])
    # Tras obtener los parametros recibidos pasamos a validar que al menos uno de los campos a actualizar esta entre ellos.
    # Si no se recibe ningun parametro, lanzamos una excepcion
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return
    # update the todo in the database
    result = todoList.update_item(
        event['pathParameters']['id'],
        data['text'], data['checked'])
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result,
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
