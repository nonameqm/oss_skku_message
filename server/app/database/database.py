from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .secrete import mysqlServer

DATABASE_URL = "mysql+mysqlconnector://"+mysqlServer.user+":"+mysqlServer.password+"@"+mysqlServer.ip+":" + mysqlServer.port+"/"+ mysqlServer.db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()