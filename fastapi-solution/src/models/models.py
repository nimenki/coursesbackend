from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid as uuid_pkg


from sqlmodel import Field, SQLModel


Base  = declarative_base()



class Course(Base):
    __tablename__ = 'course'
    id  = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    weight = Column(Integer)
    rating = Column(Float)
    url = Column(String)
    image_url = Column(String)
    price = Column(Float)
    source = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

