from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates



templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/page")


###########################################rendering##############################################
@router.get("/login")
def login_render(request:Request):
    return templates.TemplateResponse('login.html', context = {'request':request})

@router.get("/checkin")
def checkin_render(request:Request):
    return templates.TemplateResponse('checkin.html', context = {'request':request})

@router.get("/main")
def checkin_render(request:Request):
    return templates.TemplateResponse('main.html', context = {'request':request})

@router.get("/admin")
def checkin_render(request:Request):
    return templates.TemplateResponse('admin.html', context = {'request':request})

###########################################rendering##############################################
