from fastapi import FastAPI
from pydantic import BaseModel , Field
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",status_code= 200)
def main():
    return {"message":"sucessfull"}
