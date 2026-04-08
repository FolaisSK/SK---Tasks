from pydantic import BaseModel

from models.enums import Grades


class Enrollment(BaseModel):
    id: int
    student_id: str
    course_id: str
    grade: Grades | None