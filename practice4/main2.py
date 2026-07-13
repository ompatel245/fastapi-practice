from fastapi import FastAPI
from pydantic import BaseModel , Field
app = FastAPI()

class users(BaseModel):
    id : int = Field(alias="user id" ,ge= 0 , le=100 ,examples=[12])
    name : str = Field(max_length=20 , min_length=2 , alias= "username" , examples=["om"])

@app.post("/")
def create_user(data:users):
    print(users)
    return {"message":data} 