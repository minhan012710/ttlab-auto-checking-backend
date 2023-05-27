# api.py (v1.0.0)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# packages
from .v1.checking import router
from ..helpers.exception_handler import exception_types

# settings
from ..core.security import config

# init application
app = FastAPI(
    title = config["APP_NAME"],
    description = "This API was built with FastAPI. Plugin/module in TIMS that supported about cheking of employees.",
    version = "1.0.0",
    servers = [
        {
            "url": "http://localhost:9000",
            "description": "Development Server"
        },
        {
            "url": "https://philosophical-cat-uit4rn.p5sevkwj.traefikhub.io/",
            "description": "Mock Server",
        }
    ],
    exception_handlers = exception_types
)

# cors-header-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins = config["ORIGINS"],
    allow_credentials = config["CREDENTIALS"],
    allow_methods = config["METHODS"],
    allow_headers = config["HEADERS"],
)

# add router cluster
app.include_router(router)