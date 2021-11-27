from fastapi import FastAPI, Depends, Request,Form, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, RedirectResponse

from database import schema, crud
from database.database import SessionLocal, engine
from database import model
from typing import List

from routes import keyword, message, page, user
import uvicorn

def create_app():
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/templates", StaticFiles(directory="templates"), name="templates")    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "*"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(keyword.router)
    app.include_router(message.router)
    app.include_router(page.router)
    app.include_router(user.router)
    


    return app



# model.Base.metadata.create_all(bind=engine)
app=create_app()

if __name__=="__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)





