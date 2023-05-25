import json
import logging
import todoList


def create(event, context):
    data = json.loads(event['body'])
    # Tras cargar en la variable data el contenido de las variables,
    # pasamos a comprobar que tengamos el parametro text, que es requerido
    if 'text' not in data:
        logging.error("Validation failed")
        raise Exception("Couldn't create the todo item.")
    # Una vez validado anyadimos el registro en la tabla
    item = todoList.put_item(data['text'])
    # create a response with id as part of response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response
