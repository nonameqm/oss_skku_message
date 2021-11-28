from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates



templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/page")


###########################################rendering##############################################
@router.get("/login")
def login_render(request:Request):
    return templates.TemplateResponse('pages/login.html', context = {'request':request})

@router.get("/checkin")
def checkin_render(request:Request):
    return templates.TemplateResponse('pages/checkin.html', context = {'request':request})

@router.get("/main/{uid}")
def checkin_render(request:Request, uid:str):
    return templates.TemplateResponse('pages/main_page.html', context = {'request':request, 'user':uid})

@router.get("/admin")
def checkin_render(request:Request):
    return templates.TemplateResponse('pages/admin.html', context = {'request':request})

###########################################rendering##############################################

from fastapi import APIRouter, Request,  Depends
from fastapi.templating import Jinja2Templates
from database.database import SessionLocal
from sqlalchemy.orm import Session
from database import schema, crud


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/page")


###########################################rendering##############################################
@router.get("/login")
def login_render(request:Request):
    return templates.TemplateResponse('pages/login.html', context = {'request':request})

@router.get("/checkin")
def checkin_render(request:Request):
    return templates.TemplateResponse('pages/checkin.html', context = {'request':request})

@router.get("/main")
def checkin_render(request:Request, db: Session = Depends(get_database_session)):
    message_list = crud.get_msgs(db=db)
    context={
        'request': request, 
        'data': message_list
    }
    return templates.TemplateResponse('pages/main_page.html', context = context)

@router.get("/admin")
def checkin_render(request:Request):
    return templates.TemplateResponse('pages/admin.html', context = {'request':request})

###########################################rendering##############################################

