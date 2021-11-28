from fastapi import APIRouter, Request, Depends, Form
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from starlette.responses import RedirectResponse
from database.database import SessionLocal
from database import schema, crud
import urllib


templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/message")

###########################################message table##############################################
#####message#####

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/message" ,response_model=List[schema.MessageReturn])
async def read_msgs(request: Request, db: Session = Depends(get_database_session)):
    records = crud.get_msgs(db=db)
    return records

@router.get("/message/{mid}",response_model=schema.MessageReturn)
def read_msg(request:Request, mid:int, db: Session = Depends(get_database_session)):

    item = crud.get_msg(db=db,msg_id = mid)
    if item is None:
        raise HTTPException(status_code=404, detail="msg not found")

    return item

@router.get("/message/keyword/{keyword}",response_model=List[schema.MessageReturn])
async def read_msg_keyword(request:Request, keyword:str, db: Session = Depends(get_database_session)):
    item = crud.get_msg_by_keyword(db=db, keyword = keyword)
    if item is None:
        raise HTTPException(status_code=404, detail="msg not found")

    return item

@router.get("/message/user_keyword/{user}",response_model=List[schema.MessageReturn])
def read_msg_user_keyword(request:Request, uid:str, db: Session = Depends(get_database_session)):

    item = crud.get_msg_by_user_keyword(db=db, uid = uid)
    if not item:
        raise HTTPException(status_code=404, detail="msg not found")

    return item
    
#####read#####

#####create#####
@router.post('/message_keyword')
async def create_msg( db:Session = Depends(get_database_session),title:str=Form(...), contents:str=Form(...), keyword1:str = Form(...),keyword2:str = Form(...),keyword3:str = Form(...)):

    msg = schema.Message(title=title, contents = contents, datetime = datetime.now())
    keywords = list(set([keyword1, keyword2, keyword3]))
    if 'none' in keywords:
        keywords.remove('none')
    print(keywords)
    response = crud.create_msg(db = db, msg=msg, keywords = keywords)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/page/admin',status_code=303)
    return response
#####create#####
###########################################message 