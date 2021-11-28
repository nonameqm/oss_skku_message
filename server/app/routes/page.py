
from fastapi import APIRouter, Request,  Depends
from fastapi.exceptions import HTTPException
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

@router.get("/main/{uid}")
def checkin_render(request:Request, uid:str,db: Session = Depends(get_database_session)):
    message_list = crud.get_msgs(db=db)
    userinfo = crud.get_user(db = db, user_id=uid)
    keywords = crud.get_keyword_by_uid(db = db, uid = uid)
    context={
        'request': request, 
        'data': message_list,
        'user': userinfo,
        'keywords':keywords
    }
    return templates.TemplateResponse('pages/main_page.html', context = context)

@router.get("/admin")
def checkin_render(request:Request):
    return templates.TemplateResponse('pages/admin.html', context = {'request':request})
    
###########################################rendering##############################################

