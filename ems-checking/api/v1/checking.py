# checking.py
import jwt
import json
import requests
from datetime import datetime, timedelta
from fastapi import APIRouter, Request, Depends, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPBasic

# package
from ...core.schema import *
from ...core.security import *
from ...services.eac_service import *
from ...mocks.response import *
from ...mocks.response_content_docs import *
from ...helpers.exception_handler import CustomResponse
from training.src.delete_member import delete_user

# security
oauth_scheme = HTTPBearer(scheme_name='tims token')
app_scheme = HTTPBearer(scheme_name='app token')


# init router and operation
router = APIRouter(
    prefix="/eac-ai/api/v1/checking",
    tags=["EAC-AI"],
    dependencies=[],
    responses={},
)


@router.post(
    "/user", 
    summary = "add new user into json database", 
    responses = res_of_add_user_api
)
async def add_member(response: Response, item: Member, token: str = Depends(oauth_scheme)):
    """add new user api"""
    result = VerifyToken(token.credentials).verify()
    print(result)

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        response = CustomResponse(
            http_code = 401, 
            message = "UNAUTHORLIZATION", 
            error = []
        ).getResponse()
        return JSONResponse(status_code = 401, content = response)
    return add_new_member(member = item)


@router.delete(
    "/user", 
    summary = "delete a user into json database", 
    responses = res_of_delete_user_api
)
async def delete_member(response: Response, item: Emiliation, token: str = Depends(oauth_scheme)):
    """delete user api"""
    result = VerifyToken(token.credentials).verify()
    email = item.email

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        response = CustomResponse(
            http_code = 401, 
            message = "UNAUTHORLIZATION", 
            error = []
        ).getResponse()
        return JSONResponse(status_code = 401, content = response)
    delete_user(email)
    response = CustomResponse(
        http_code = 200, 
        message = "Success"
    ).getResponse()
    return JSONResponse(status_code = 200, content = response)


@router.post(
    "/", 
    summary = "checking user"
)
async def checking(item: Detection, token: str = Depends(app_scheme)):
    """recogny user api"""
    return checking_member(item.image, item.checking_type, token)