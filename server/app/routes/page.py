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

@router.get("/main")
def checkin_render(request:Request):
    return templates.TemplateResponse('pages/main_page.html', context = {'request':request})

@router.get("/admin")
def checkin_render(request:Request):
    return templates.TemplateResponse('pages/admin.html', context = {'request':request})

###########################################rendering##############################################
