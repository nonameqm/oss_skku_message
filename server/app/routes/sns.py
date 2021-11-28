from fastapi import APIRouter, Request, Depends, Form
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from starlette.responses import RedirectResponse
from database.database import SessionLocal
from database import schema, crud


templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/sns")


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/insta/all", response_model = List[schema.Insta])
async def read_insta_all(request:Request, db:Session = Depends(get_database_session)):
    item = crud.get_insta(db=db)
    return item

@router.get("/youtube/all", response_model = List[schema.Youtube])
async def read_youtube_all(request:Request, db:Session = Depends(get_database_session)):
    item = crud.get_youtube(db=db)
    return item

@router.get("/insta/{title}}", response_model = schema.Insta)
async def read_insta_id(request:Request,title:str, db:Session = Depends(get_database_session)):
    item = crud.get_insta_by_title(db=db, title=title)
    return item

@router.get("/youtube/{title}", response_model = schema.Youtube)
async def read_youtube_id(request:Request,title:str, db:Session = Depends(get_database_session)):
    item = crud.get_youtube_by_title(db=db, title = title)
    return item

@router.post("/insta_add")
async def create_insta(request:Request, db:Session = Depends(get_database_session), title:str = Form(...), url:str = Form(...)):
    insta = schema.Insta(title = title, url = url)
    item = crud.create_insta(db=db, insta= insta)
    if item != None:
        return HTTPException(status_code=200, detail="Success")
    else:
        return HTTPException(status_code=404, detail="Fail")

@router.post("/youtube_add")
async def create_youtube(request:Request, db:Session = Depends(get_database_session), title:str = Form(...), url:str = Form(...)):
    youtube = schema.Youtube(title = title, url = url)
    item = crud.create_youtube(db=db, youtube=youtube)
    if item != None:
        return HTTPException(status_code=200, detail="Success")
    else:
        return HTTPException(status_code=404, detail="Fail")

