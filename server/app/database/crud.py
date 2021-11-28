from sqlalchemy.orm import Session
from sqlalchemy import func, distinct
from database import model, schema
from sqlalchemy.types import String, Integer, Text




def get_user(db: Session, user_id: str):
    return db.query(model.User).filter(model.User.uid == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.User):
    db_user = model.User(**user.dict())
    if get_user_by_email(db, user.uid) != None:
        return None
    else:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

def update_user_keyword(db:Session, uid:str, keywords:str):
    db_user=db.query(
        model.User
    ).filter(
        model.User.uid == uid
    ).update(
        {'keywords':keywords}
    )
    db.commit()
    return db_user


def get_msg(db: Session, msg_id: int):
    return db.query(model.Message).filter(model.Message.mid == msg_id).first()

def get_msg_by_keyword(db:Session, keyword:str):
    obj = db.query(model.Message).join(
        model.Keyword,
        model.Keyword.mid == model.Message.mid
    ).filter(
        model.Keyword.keyword == keyword
    ).all()
    return obj



def get_msgs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Message).offset(skip).limit(limit).all()

def get_last_msg_id_by_int(db: Session):
    mid = db.query(func.max(model.Message.mid)).scalar()
    return mid


def create_msg(db: Session, msg: schema.Message, keywords):
    db_msg = model.Message(**msg.dict())

    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)

    mid = get_last_msg_id_by_int(db)
    for keyword in keywords:
        db_keyword = model.Keyword(**(schema.Keyword(mid = mid, keyword = keyword).dict()))
        db.add(db_keyword)
        db.commit()
        db.refresh(db_keyword)
    return db_msg

def get_keyword(db: Session, keyword: str):
    return db.query(model.Keyword).filter(model.Keyword.keyword == keyword).first()


def get_keywords(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Keyword.keyword).distinct().all()


def get_keywords_by_keyword(db: Session, keyword: str):
    return db.query(model.Keyword).filter(model.Keyword.keyword == keyword).all()

def create_keyword(db: Session, keyword: schema.Keyword):
    db_keyword = model.Keyword(**keyword.dict())
    if get_keyword(db, keyword.keyword) != None:
        return None
    else:
        db.add(db_keyword)
        db.commit()
        db.refresh(db_keyword)
        return db_keyword


def get_keyword_by_uid(db:Session, uid:str):
    obj = db.query(model.Keyword ).join(
        model.UserKeyAssoc,
        model.Keyword.relation_id == model.UserKeyAssoc.relation_id
    ).all()
    return obj

def get_msg_by_user_keyword(db:Session, uid:str):
    obj = db.query(model.Message).join(
        model.Keyword,
        model.Keyword.mid == model.Message.mid
    ).join(
        model.UserKeyAssoc,
        model.UserKeyAssoc.relation_id == model.Keyword.relation_id and model.UserKeyAssoc.user_id == uid
    ).all()
    return obj

def get_insta(db:Session):
    item = db.query(model.Insta).all()
    return item

def get_youtube(db:Session):
    item = db.query(model.Insta).all()
    return item

def get_insta_by_title(db:Session, title:str):
    item = db.query(model.Insta).filter(model.Insta.title == title).first()
    return item

def get_youtube_by_title(db:Session, title:str):
    item = db.query(model.Youtube).filter(model.Youtube.title == title).first()
    return item

def create_insta(db:Session, insta:schema.Insta):
    db_insta = model.Insta(**insta.dict())
    db.add(db_insta)
    db.commit()
    db.refresh(db_insta)
    return db_insta

def create_youtube(db:Session, youtube:schema.Youtube):
    db_youtube = model.Youtube(**youtube.dict())
    db.add(db_youtube)
    db.commit()
    db.refresh(db_youtube)
    return db_youtube

