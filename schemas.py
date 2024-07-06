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
    