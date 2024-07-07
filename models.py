from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index = True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    applications = relationship("Application", back_populates = "user")
class Application(Base):
    __tablename__ = "apps"

    app_id = Column(Integer, primary_key=True)
    link = Column(String)
    company = Column(String)
    role = Column(String)
    date_applied = Column(String)
    date_heard_back = Column(String)
    industry = Column(String)
    location = Column(String)
    application_platform = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates = "applications")
    