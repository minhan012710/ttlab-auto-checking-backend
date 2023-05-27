# exception_handler.py 
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi import Request
import json
from enum import Enum

# package
from .types import *

# define response status
class ResponseStatus(Enum):
    '''enum response status'''
    SUCCESS = 200
    BAD_REQUEST = 400
    UNAUTHORLIZATION = 401
    FOR_BIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


# define response
class CustomResponse:
    '''define custom response in project'''
    def __init__(self, http_code, message, data = [], error = [], version = "1.0.0"):
        self.http_code = http_code
        self.message = message
        self.data = data
        self.error = error
        self.version = version

    def getHttpCode(self):
        return self.http_code

    def getMessage(self):
        return self.message

    def getData(self):
        return self.data

    def getError(self):
        return self.error

    def getResponse(self):
        if self.http_code == 200:
            return Ok(message = self.message, data = self.data, version = self.version)
        else:
            return Error(message = self.message, error = self.error, version = self.version)


# overide http exception
class CustomException(HTTPException):
    '''overide http exception'''
    pass


# define default response
async def not_found(request: Request, exc: CustomException):
    return JSONResponse(status_code = 404, content = Error(message = "NOT FOUND"))

async def internal_server_error(request: Request, exc: CustomException):
    return JSONResponse(status_code = 500, content = Error(message = "INTERNAL SERVER ERROR"))

async def for_bidden(request: Request, exc: CustomException):
    return JSONResponse(status_code = 403, content = Error(message = "FOR BIDDEN"))


# exception default
exception_types = {
    ResponseStatus.NOT_FOUND.value: not_found,
    ResponseStatus.INTERNAL_SERVER_ERROR.value: internal_server_error,
    ResponseStatus.FOR_BIDDEN.value: for_bidden
}