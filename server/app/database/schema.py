from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    uid: str
    email: str
    name: str
    password: str
    keyword:str
    
    class Config:
        orm_mode = True


class Message(BaseModel):
    
    title:str
    contents: str
    datetime: datetime
    class Config:
        orm_mode = True

class MessageReturn(Message):
    mid: int


class Keyword(BaseModel):
    
    keyword : str
    mid:int
    class Config:
        orm_mode = True

class KeywordsDistinct(BaseModel):
    keyword : str
    class Config:
        orm_mode = True

class KeywordReturn(Keyword):
    relation_id: int

class UserKeyAssoc(BaseModel):
    user_id:str
    relation_id:int
    class Config:
        orm_mode = True

