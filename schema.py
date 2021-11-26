from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    uid: str
    email: str
    name: str
    password: str
    
    class Config:
        orm_mode = True


class Message(BaseModel):
    mid:int
    contents: str
    class Config:
        orm_mode = True


class Keyword(BaseModel):
    keyword : str
    class Config:
        orm_mode = True

class UserKeyAssoc(BaseModel):
    uid:str
    keyword:str
    class Config:
        orm_mode = True

class MsgKeyAssoc(BaseModel):
    mid:int
    keyword:str
    class Config:
        orm_mode = True