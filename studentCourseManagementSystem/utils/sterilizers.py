from models.course import Course
from models.enrollment import Enrollment
from models.user import User


def map_user(user: User):
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'role': user.role
    }

def map_course(course: Course):
    return {
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'facilitator_id': course.facilitator_id
    }
def map_enrollment(enrollment: Enrollment):
    return {
        'id': enrollment.id,
        'course_id': enrollment.course_id,
        'student_id': enrollment.student_id,
        'grade': enrollment.grade,
    }