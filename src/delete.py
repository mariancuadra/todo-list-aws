import todoList


def delete(event, context):
    # Da por sentado que recibimos como parametro el identificador a eliminar
    # Podria mejorarse haciendo una previa validacion
    todoList.delete_item(event['pathParameters']['id'])

    # create a response
    response = {
        "statusCode": 200
    }

    return response
