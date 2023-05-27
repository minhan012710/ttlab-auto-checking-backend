def data(name = "unknown"):
    return {
        "id": 1,
        "email": "email@example.com",
        "name": name
    }

def error(key, message):
    error_result = [
        {
            "key": key,
            "errorCode": 400,
            "message": message
        }
    ]
    return error_result