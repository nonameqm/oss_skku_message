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

@router.post("change_keyword/{uid}")
def change_keyword(request:Request, uid: str, db: Session = Depends(get_database_session), keywords:str = Form(...)):

    item = crud.update_user_keyword(db=db, uid = uid, keywords=keywords)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")

    return HTTPException(status_code=200, detail="success")

@router.post("/login")
def logincheck(db:Session = Depends(get_database_session), id:str = Form(...), password:str=Form(...)):
    item = crud.get_user(db=db, user_id = id)
    response =  HTTPException(status_code=412, detail="Password fail")
    if item.password == password:
        response =  RedirectResponse('/page/main/{}'.format(id),status_code=303)
        if item.uid == "admin":
            response =  RedirectResponse('/page/admin',status_code=303)
    return response
#####read#####

#####create#####
@router.post('/enroll')
async def create_user( db:Session = Depends(get_database_session), id:str = Form(...), email:str=Form(...), name:str = Form(...), password:str = Form(...)):
    user = schema.User(uid = id, email = email, name = name, password = password, keywords="")
    response = crud.create_user(db = db, user=user)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/page/login',status_code=303)
    return response
#####create#####
###########################################user table##############################################

