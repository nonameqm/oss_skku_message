from sqlalchemy.schema import Column
from sqlalchemy import ForeignKey, Table, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.types import String, Integer, Text
from database.database import Base


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


class User(Base):
    __tablename__ = "users"
    __table_args__= (
        {
            "mysql_default_charset": "utf8"
        }
    )
    uid = Column(String(20), primary_key=True)
    email = Column(String(50), unique=True)
    name = Column(String(20))
    password = Column(String(50))
    keywords = Column(Text)

class Message(Base):
    __tablename__ = "messages"
    __table_args__= (
        {
            "mysql_default_charset": "utf8"
        }
    )
    mid = Column(Integer, primary_key=True, unique= True, autoincrement=True)
    title = Column(String(100))
    contents = Column(Text)
    datetime = Column(DateTime)
    Key = relationship("Keyword", back_populates="msg")

class Keyword(Base):
    __tablename__ = "keywords"
    __table_args__= (
        {
            "mysql_default_charset": "utf8"
        }
    )
    relation_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    mid = Column(ForeignKey(Message.mid))
    keyword = Column(String(20))
    msg = relationship("Message", back_populates="Key")
    

# class UserKeyAssoc(Base):
#     __tablename__ = "user_key_assoc"
#     __table_args__ = (
#         PrimaryKeyConstraint('user_id', 'relation_id'),
#     )

#     user_id = Column(ForeignKey('users.uid'))
#     relation_id = Column(ForeignKey('keywords.relation_id'))
