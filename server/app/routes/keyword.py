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
@router.get("/all_distinct")
async def read_keywords(request: Request, db: Session = Depends(get_database_session)):
    records = crud.get_keywords(db=db)
    print(records)
    return records

@router.get("/{keyword}",response_model=schema.KeywordReturn)
def read_keyword(request:Request, keyword: str, db: Session = Depends(get_database_session)):

    records = crud.get_keyword(db=db, keyword = keyword)
    if records is None:
        raise HTTPException(status_code=404, detail="User not found")

    return records
#####read#####


@router.get('/user_id/{uid}', response_model=List[schema.KeywordReturn])
async def get_user_keys(request:Request, uid:str, db:Session = Depends(get_database_session)):
    response = crud.get_keyword_by_uid(db=db, uid=uid)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    
    return response

@router.post('/user_key_add')
async def create_user_key_assoc( db:Session = Depends(get_database_session), id:str = Form(...), keyword:str=Form(...)):
    msg_key_relation = crud.get_keywords_by_keyword(db= db, keyword=keyword)

    relation_ids = []
    for row in msg_key_relation:
        relation_ids.append(row.relation_id)
    
    for relation_id in relation_ids:
        assoc = schema.UserKeyAssoc(user_id = id,relation_id = relation_id)
        response = crud.create_user_key_assoc(db=db, user_key_assoc=assoc)
    if response == None:
        raise HTTPException(status_code=412, detail="User ID already exists")
    response = HTTPException(status_code=201, detail="Keyword Created")



 
