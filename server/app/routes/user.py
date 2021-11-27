from fastapi import APIRouter, Request, Depends, Form
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from starlette.responses import RedirectResponse
from database.database import SessionLocal
from database import schema, crud


templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/user")


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

###########################################user table##############################################
#####read#####
@router.get("/", response_model=List[schema.User])
async def read_Users(request: Request, db: Session = Depends(get_database_session)):
    records = crud.get_users(db=db)
    return records

@router.get("/{uid}",response_model=schema.User)
def read_User(request:Request, uid: str, db: Session = Depends(get_database_session)):

    item = crud.get_user(db=db, user_id = uid)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse("html", {"request": request, "User": item})
#####read#####

#####create#####
@router.post('/')
async def create_user( db:Session = Depends(get_database_session), id:str = Form(...), email:str=Form(...), name:str = Form(...), password:str = Form(...)):
    user = schema.User(uid = id, email = email, name = name, password = password)
    response = crud.create_user(db = db, user=user)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/page/login',status_code=303)
    return response
#####create#####
###########################################user table##############################################

