from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    description: str
    facilitator_name: str