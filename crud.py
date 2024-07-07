from sqlalchemy.orm import Session

from . import models, schemas

"""
Utility functions to read data
    get_job_app reads the application by application id
    get_job_apps reads multiple applications
    get_user read a single user by ID 
    get_user_by_email read a single user by email 
"""

def get_job_app(db : Session, app_id : int):
    return db.query(models.Application).filter(models.Application.app_id == app_id).first()

def get_job_apps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Application).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

""" 
Utility functions to create data

"""
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_application(db: Session, application: schemas.ApplicationCreate, user_id: int):
    db_application = models.Application(**application.model_dump(), user = user_id)
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application 