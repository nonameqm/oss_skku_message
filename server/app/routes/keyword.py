from fastapi import APIRouter, Request, Depends, Form
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from starlette.responses import RedirectResponse
from database.database import SessionLocal
from database import schema, crud


templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/keyword")


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

###########################################keyword table##############################################
#####read#####
@router.get("/")
async def read_Users(request: Request, db: Session = Depends(get_database_session)):
    records = crud.get_users(db=db)
    return records

@router.get("/{keyword}",response_model=schema.User)
def read_User(request:Request, uid: str, db: Session = Depends(get_database_session)):

    item = crud.get_user(db=db, user_id = uid)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse("html", {"request": request, "User": item})
#####read#####

#####create#####
@router.post('/')
async def create_keyword( db:Session = Depends(get_database_session), keyword:str = Form(...)):
    keyWord = schema.Keyword(keyword = keyword)
    response = crud.create_keyword(db = db, keyword = keyWord)
    if response == None:
        raise HTTPException(status_code=412, detail="Keyword already exists")
    response = RedirectResponse('/main',status_code=303)
    return response



@router.post('/user_key_add')
async def create_user_key_assoc( db:Session = Depends(get_database_session), id:str = Form(...), keyword:str=Form(...)):
    assoc = schema.UserKeyAssoc(uid = id, keyword = keyword)
    response = crud.create_user_key_assoc(db=db, user_key_assoc=assoc)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/login',status_code=303)
    return response

@router.post('/user_key_msg')
async def get_msg_user_key( db:Session = Depends(get_database_session), id:str = Form(...)):
    
    response = crud.get_msg_by_user_key(db=db, uid=id)
    print(response)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/login',status_code=303)
    return response
 
