# schema.py
from pydantic import BaseModel,  Field
from typing import Union

# class 
class Member(BaseModel):
    email: str = Field(example = "abc@tokyotechlab.com")
    images: str = Field(example = "base64 base64 base64 base64 base64")

    class Config:
        schema_extra = {
            "example": {
                "images": "base64 base64 base64 base64 base64",
                "email": "abc@tokyotechlab.com"
            }
        }


class Detection(BaseModel):
    image: str = Field(example = "base64-string")
    checking_type: str = Field(example = "check_in/check_out")

    class Config:
        schema_extra = {
            "example":{
                "image": "base64",
                "checking_type": "check_in/check_out"
            }
        }

class Emiliation(BaseModel):
    email: str = Field(example = "abc@tokyotechlab.com")
    schema_extra = {
            "example": [
                {
                    "email": "abc@tokyotechlab.com"
                }
            ],
        }