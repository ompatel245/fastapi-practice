from fastapi import FastAPI
from pydantic import BaseModel , Field

app = FastAPI()


class firstdata(BaseModel):
    name : str = Field(default="om")
    roll : int = Field(default= 9)

class seconddata(BaseModel):
    divison : str = Field(default="A")
    address : firstdata

@app.post("/{id}")
def home(var : firstdata, id : int, name : str = None):
    var.roll = id
    var.name = name
    return var

@app.post("/home/")
def addresshome(var : seconddata):
    print(var)
    return var

@app.put("/")
def putmeth(var : firstdata):
    print(var)
    return var