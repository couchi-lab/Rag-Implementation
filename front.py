import os
from os.path import join, dirname
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["127.0.0.1"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "DSN": DSN,
        "USN": USN,
        "PWD": PWD
    }
print(DSN, USN, PWD)