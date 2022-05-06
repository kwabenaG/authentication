# main.py ==== >  just for a authentication test

import os
from fastapi import FastAPI


# create an instance  of fastapi 
app = FastAPI()


# create endpoints

@app.get("/")
def homepage():
    return {"message": "Hello World"}

