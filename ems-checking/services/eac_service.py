from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image

# module training
from training.src.make_data_train import Trainer
from training.src.face_rec import Face_recognition

# package
from ..helpers.base64_convert import *
from ..mocks.response import *
from ..helpers.exception_handler import CustomResponse

# settings
from ..core.security import config

# init recognization
face_recogny = Face_recognition()

def add_new_member(member):
    '''add images of new user in json db'''
    try:
        trainer = Trainer()
        list_base64 = member.images.split(" ")
        list_img = [stringToRGB(i) for i in list_base64]
        # one of images have not any face
        for img in list_img:
            if trainer.add_member(image = img, email = member.email) == None:
                result = error(
                    key = "images", 
                    message = "can not recogny face from images"
                )
                response = CustomResponse(
                    http_code = 400, 
                    message = "Bad Request", 
                    error = result
                ).getResponse()
                return JSONResponse(status_code = 400, content = response)
        # success
        response = CustomResponse(
            http_code = 200, 
            message = "Success"
        ).getResponse()
        return JSONResponse(status_code = 200, content = response)
    except:
        # bad request
        result = error(
            key = "images", 
            message = "images is invalid"
        )
        response = CustomResponse(
            http_code = 400, 
            message = "Bad Request", 
            error = result
        ).getResponse()
        return JSONResponse(status_code = 400, content = response)

def checking_member(image, checking_type, token):
    '''checking member from image'''
    try:
        image = stringToRGB(image)
        result = face_recogny.recogny_face(image)
        # image have not any face
        if result == None:
            result = error(
                key = "image", 
                message = "image is invalid"
            )
            response = CustomResponse(
                http_code = 400, 
                message = "Bad Request", 
                error = result
            ).getResponse()
            return JSONResponse(status_code = 400, content = response)
        # recogny
        frame, bbox, email, current_time = result
        frame_b64 = RGB2String(result[0])
        if email == "Unknown":
            result = error(
                key = "image", 
                message = "can not recogny member"
            )
            response = CustomResponse(
                http_code = 400, 
                message = "Bad Request", 
                error = result
            ).getResponse()
            return JSONResponse(status_code = 400, content = response)
        else:
            # send request to tims
            auth_token = get_token()
            headers = {"authorization": "Bearer " + auth_token}
            data = {
                "email": "lehieugch6898@gmail.com",
                "checkingType": item.checking_type,
                "token": token.credentials
            }
            response = requests.post(config["TIMS_URL"], json = data, headers = headers)
            print(response.text) 
            conn.close()
            # success
            response = CustomResponse(
                http_code = 200, 
                message = "Success", 
                data = data(email)
            ).getResponse()
            return JSONResponse(status_code = 200, content = response)
    except:
        # base64 invalid
        result = error(
            key = "image", 
            message = "base64 is not an instance of images"
        )
        response = CustomResponse(
            http_code = 400, 
            message = "Bad Request", 
            error = result
        ).getResponse()
        return JSONResponse(status_code = 400, content = response)