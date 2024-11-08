from pydantic import BaseModel
from datetime import datetime

class Project(BaseModel):
    title: str
    description: str
    time_to_complete: int

class GetProject(Project):
    id: str
    status: str
    created: datetime
    deadline: datetime