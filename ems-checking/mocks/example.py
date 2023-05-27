res_of_add_user_api = {
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "example": {
                    "message": "Bad Request",
                    "errors": [
                        {
                            "key": "image",
                            "errorCode": 400,
                            "message": "image is invalid"
                        }
                    ],
                    "version": "1.0.0"
                }
            }
        },
    },
    200: {
        "description": "Successfully Response",
        "content": {
            "application/json": {
                "example": {
                    "message": "Success", 
                    "data": [],
                    "version": "1.0.0"
                }
            }
        },
    },
    422: {"model": None}
}

res_of_delete_user_api = {
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "example": {
                    "message": "Bad Request",
                    "errors": [
                        {
                            "key": "image",
                            "errorCode": 400,
                            "message": "image is invalid"
                        }
                    ],
                    "version": "1.0.0"
                }
            }
        },
    },
    200: {
        "description": "Successfully Response",
        "content": {
            "application/json": {
                "example": {
                    "id": "bar", 
                    "value": "The bar tenders"
                }
            }
        },
    },
    422: {"model": None}
}