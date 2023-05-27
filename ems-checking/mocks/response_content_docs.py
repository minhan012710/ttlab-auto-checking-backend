res_of_add_user_api = {
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
    401: {
        "description": "Unauthorlization",
        "content": {
            "application/json": {
                "example": {
                    "message": "UNAUTHORLIZATION",
                    "errors": [],
                    "version": "1.0.0"
                }
            }
        },
    },
    403: {
        "description": "For Bidden",
        "content": {
            "application/json": {
                "example": {
                    "message": "FOR BIDDEN",
                    "errors": [],
                    "version": "1.0.0"
                }
            }
        },
    },
    404: {
        "description": "Not Found",
        "content": {
            "application/json": {
                "example": {
                    "message": "NOT FOUND",
                    "errors": [],
                    "version": "1.0.0"
                }
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {
                    "message": "INTERNAL SERVER ERROR",
                    "errors": [],
                    "version": "1.0.0"
                }
            }
        },
    }
}

res_of_delete_user_api = {
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
    401: {
        "description": "Unauthorlization",
        "content": {
            "application/json": {
                "example": {
                    "message": "UNAUTHORLIZATION",
                    "errors": [],
                    "version": "1.0.0"
                }
            }
        },
    },
    403: {
        "description": "For Bidden",
        "content": {
            "application/json": {
                "example": {
                    "message": "FOR BIDDEN",
                    "errors": [],
                    "version": "1.0.0"
                }
            }
        },
    },
    404: {
        "description": "Not Found",
        "content": {
            "application/json": {
                "example": {
                    "message": "NOT FOUND",
                    "errors": [],
                    "version": "1.0.0"
                }
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {
                    "message": "INTERNAL SERVER ERROR",
                    "errors": [],
                    "version": "1.0.0"
                }
            }
        },
    }
}