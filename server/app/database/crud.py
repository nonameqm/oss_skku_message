from sqlalchemy.orm import Session
from sqlalchemy import func
from database import model, schema



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


def get_msg(db: Session, msg_id: int):
    return db.query(model.Message).filter(model.Message.mid == msg_id).first()


def get_msgs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Message).offset(skip).limit(limit).all()


def create_msg(db: Session, msg: schema.Message, keywords):
    db_msg = model.Message(**msg.dict())
    if get_msg(db, msg.mid) != None:
        return None
    else:
        db.add(db_msg)
        db.commit()
        db.refresh(db_msg)

        mid = db.query(func.max(model.Message.mid))
        for keyword in keywords:
            db_msg_key_assoc = model.MsgKeyAssoc(**(schema.MsgKeyAssoc(mid = mid, keyword = keyword).dict()))
            db.add(db_msg_key_assoc)
            db.commit()
            db.refresh(db_msg_key_assoc)
        return db_msg

def get_keyword(db: Session, keyword: str):
    return db.query(model.Keyword).filter(model.Keyword.keyword == keyword).first()


def get_keywordss(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Keyword).offset(skip).limit(limit).all()


def create_keyword(db: Session, keyword: schema.Keyword):
    db_keyword = model.Keyword(**keyword.dict())
    if get_keyword(db, keyword.keyword) != None:
        return None
    else:
        db.add(db_keyword)
        db.commit()
        db.refresh(db_keyword)
        return db_keyword

def get_user_key_assoc(db:Session, assoc: schema.UserKeyAssoc):
    obj = db.query(model.UserKeyAssoc).filter(
            model.UserKeyAssoc.uid == assoc.uid and model.UserKeyAssoc.keyword == assoc.keyword
        ).all()
    return obj

def create_user_key_assoc(db:Session, user_key_assoc: schema.UserKeyAssoc):
    
    if not get_user_key_assoc(db, assoc = user_key_assoc):
        db_usr_key_assoc = model.UserKeyAssoc(**user_key_assoc.dict())
        db.add(db_usr_key_assoc)
        db.commit()
        db.refresh(db_usr_key_assoc)
        return user_key_assoc
    else:
        return None


def get_keyword_by_uid(db:Session, assoc: schema.UserKeyAssoc):
    obj = db.query(model.UserKeyAssoc).filter(
            model.UserKeyAssoc.uid == assoc.uid
        ).all()
    return obj

def get_msg_key_assoc(db:Session, assoc: schema.MsgKeyAssoc):
    obj = db.query(model.MsgKeyAssoc).filter(
            model.MsgKeyAssoc.mid == assoc.mid and model.MsgKeyAssoc.keyword == assoc.keyword
        ).all()
    return obj



def get_msg_by_keyword(db:Session, assoc: schema.MsgKeyAssoc):
    obj = db.query(model.MsgKeyAssoc).filter(
            model.MsgKeyAssoc.keyword == assoc.keyword 
        ).all()
    return obj

def get_msg_by_user_key(db:Session, uid: str):
    obj = db.join(
        model.Message
    ).join(
        model.MsgKeyAssoc
    ).join(
        model.UserKeyAssoc
    ).filter(
        model.UserKeyAssoc.uid == uid
    ).all()

    return obj



