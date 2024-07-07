from pydantic import BaseModel

class ApplicationBase(BaseModel):
    link : str
    company : str
    role : str
    date_applied : str
    date_heard_back : str
    industry : str
    location : str
    application_platform : str

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    app_id : int
    user_id : int
    class Config:
        orm_mode = True  

class UserBase(BaseModel):
    email : str

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id : int
    is_active : bool
    applications : list[Application] = []

    class Config:
        orm_mode = True

