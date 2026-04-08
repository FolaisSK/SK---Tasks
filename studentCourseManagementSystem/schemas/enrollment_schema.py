from pydantic import BaseModel

from models.enums import Grades


class AssignGradeSchema(BaseModel):
    facilitator_id:str
    course_id: str
    student_id: str
    grade: Grades