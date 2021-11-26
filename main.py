from fastapi import FastAPI, Depends, Request,Form, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse, RedirectResponse

import schema, crud
from database import SessionLocal, engine
import model
from typing import List


model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}




###########################################rendering##############################################
@app.get("/login")
def login_render(request:Request):
    return templates.TemplateResponse('login.html', context = {'request':request})

@app.get("/checkin")
def checkin_render(request:Request):
    return templates.TemplateResponse('checkin.html', context = {'request':request})

@app.get("/main")
def checkin_render(request:Request):
    return templates.TemplateResponse('main.html', context = {'request':request})

@app.get("/admin")
def checkin_render(request:Request):
    return templates.TemplateResponse('admin.html', context = {'request':request})

###########################################rendering##############################################





###########################################user table##############################################
#####read#####
@app.get("/user", response_model=List[schema.User])
async def read_Users(request: Request, db: Session = Depends(get_database_session)):
    records = crud.get_users(db=db)
    return records

@app.get("/user/{uid}",response_model=schema.User)
def read_User(request:Request, uid: str, db: Session = Depends(get_database_session)):

    item = crud.get_user(db=db, user_id = uid)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse("html", {"request": request, "User": item})
#####read#####

#####create#####
@app.post('/user/')
async def create_user( db:Session = Depends(get_database_session), id:str = Form(...), email:str=Form(...), name:str = Form(...), password:str = Form(...)):
    user = schema.User(uid = id, email = email, name = name, password = password)
    response = crud.create_user(db = db, user=user)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/login',status_code=303)
    return response
#####create#####
###########################################user table##############################################





###########################################message table##############################################
#####message#####
@app.get("/message", response_model=List[schema.User])
async def read_msgs(request: Request, db: Session = Depends(get_database_session)):
    records = crud.get_users(db=db)
    return records

@app.get("/message/{mid}",response_model=schema.User)
def read_msg(request:Request, mid: str, db: Session = Depends(get_database_session)):

    item = crud.get_msg(db=db,msg_id = mid)
    if item is None:
        raise HTTPException(status_code=404, detail="msg not found")

    return templates.TemplateResponse("html", {"request": request, "User": item})
#####read#####

#####create#####
@app.post('/message/')
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
###########################################message table##############################################





###########################################keyword table##############################################
#####read#####
@app.get("/keyword")
async def read_Users(request: Request, db: Session = Depends(get_database_session)):
    records = crud.get_users(db=db)
    return records

@app.get("/keyword/{keyword}",response_model=schema.User)
def read_User(request:Request, uid: str, db: Session = Depends(get_database_session)):

    item = crud.get_user(db=db, user_id = uid)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse("html", {"request": request, "User": item})
#####read#####

#####create#####
@app.post('/keyword/')
async def create_keyword( db:Session = Depends(get_database_session), keyword:str = Form(...)):
    keyWord = schema.Keyword(keyword = keyword)
    response = crud.create_keyword(db = db, keyword = keyWord)
    if response == None:
        raise HTTPException(status_code=412, detail="Keyword already exists")
    response = RedirectResponse('/main',status_code=303)
    return response 
#####create#####
###########################################user table##############################################



@app.post('/user_key_add')
async def create_user_key_assoc( db:Session = Depends(get_database_session), id:str = Form(...), keyword:str=Form(...)):
    assoc = schema.UserKeyAssoc(uid = id, keyword = keyword)
    response = crud.create_user_key_assoc(db=db, user_key_assoc=assoc)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/login',status_code=303)
    return response

@app.post('/user_key_msg')
async def get_msg_user_key( db:Session = Depends(get_database_session), id:str = Form(...)):
    
    response = crud.get_msg_by_user_key(db=db, uid=id)
    print(response)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = RedirectResponse('/login',status_code=303)
    return response
