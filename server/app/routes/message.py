from fastapi import APIRouter, Request, Depends, Form
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from starlette.responses import RedirectResponse
from database.database import SessionLocal
from database import schema, crud


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

@router.get("/message", response_model=List[schema.User])
async def read_msgs(request: Request, db: Session = Depends(get_database_session)):
    records = crud.get_users(db=db)
    return records

@router.get("/message/{mid}",response_model=schema.User)
def read_msg(request:Request, mid: str, db: Session = Depends(get_database_session)):

    item = crud.get_msg(db=db,msg_id = mid)
    if item is None:
        raise HTTPException(status_code=404, detail="msg not found")

    return templates.TemplateResponse("html", {"request": request, "User": item})
#####read#####

#####create#####
@router.post('/message/')
async def create_msg( db:Session = Depends(get_database_session), contents:str=Form(...), keyword1:str = Form(...),keyword2:str = Form(...),keyword3:str = Form(...)):
    msg = schema.Message(contents = contents)
    keywords = [keyword1,keyword2,keyword3]
    keywords = keywords.remove('none')
    response = crud.create_msg(db = db, msg=msg, keywords = keywords )
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/main',status_code=303)
    return response
#####create#####
###########################################message 