from endpoint import router  # Import your router
import config
import shutil
from typing import Annotated
from fastapi import FastAPI, Form, File, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from fraction import get_fractions_FMI_parallel
import json
from utils import load_process
import json
app = FastAPI()


app = FastAPI()

origins = [config.ORIGIN]  # Update with your frontend origin

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api",)  # Include the router
