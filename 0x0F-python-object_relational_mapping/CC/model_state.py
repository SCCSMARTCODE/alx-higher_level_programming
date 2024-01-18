#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
  __tablename__ = 'states'
  id = Column(Integer,primary_key=True,autoincrement=True,unique=True,nullable=False)
  name = Column(String(128),nullable=False)
  
