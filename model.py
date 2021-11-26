from sqlalchemy.schema import Column
from sqlalchemy import ForeignKey, Table, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import String, Integer, Text
from database import Base

# messgae_key_association_table = Table(
#     'msg_key_association', 
#     Base.metadata,
#     Column('msg_id', ForeignKey('messages.mid')),
#     Column('keyword', ForeignKey('keywords.keyword'))
# )

# user_key_association_table = Table(
#     'user_key_association', 
#     Base.metadata,
#     Column('user_id', ForeignKey('users.uid')),
#     Column('keyword', ForeignKey('keywords.keyword'))
# )

class UserKeyAssoc(Base):
    __tablename__ = "user_key_assoc"
    __table_args__ = (
        PrimaryKeyConstraint('uid', 'keyword'),
    )

    uid = Column(ForeignKey('users.uid'))
    keyword = Column(ForeignKey('keywords.keyword'))

class MsgKeyAssoc(Base):
    __tablename__ = "msg_key_assoc"
    __table_args__ = (
        PrimaryKeyConstraint('mid', 'keyword'),
    )
    mid = Column(ForeignKey('messages.mid'))
    keyword = Column(ForeignKey('keywords.keyword'))


class User(Base):
    __tablename__ = "users"
    uid = Column(String(20), primary_key=True)
    email = Column(String(50), unique=True)
    name = Column(String(20))
    password = Column(String(50))
    

class Message(Base):
    __tablename__ = "messages"
    mid = Column(Integer, primary_key=True, unique= True, autoincrement=True)
    contents = Column(String(500))


class Keyword(Base):
    __tablename__ = "keywords"
    keyword = Column(String(20), primary_key=True)