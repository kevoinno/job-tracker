from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class ApplicationsBase(Base):
    __tablename__ = "apps"

    id = Column(Integer, primary_key=True)
    link = Column(String)
    company = Column(String)
    role = Column(String)
    date_applied = Column(String)
    date_heard_back = Column(String)
    industry = Column(String)
    location = Column(String)
    application_platform = Column(String)
    
class ApplicationsCreate(ApplicationsBase):
    pass

class Application(ApplicationsBase):
    id : int
    
    class Config:
        orm_mode = True