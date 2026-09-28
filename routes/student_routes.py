from fastapi import APIRouter, status
from models.student_model import Student, StudentCreate, StudentUpdate
from controllers import student_controller

# Create router for student endpoints
router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# 1. Create Student
@router.post(
    "",
    response_model=Student,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new student",
    description="Add a new student record to the local memory storage."
)
def create_student(student: StudentCreate):
    return student_controller.create_student(student)


# 2. Read All Students
@router.get(
    "",
    response_model=list[Student],
    status_code=status.HTTP_200_OK,
    summary="Read all students",
    description="Retrieve a list of all enrolled students."
)
def get_all_students():
    return student_controller.get_all_students()


# 3. Read Student by ID
@router.get(
    "/{id}",
    response_model=Student,
    status_code=status.HTTP_200_OK,
    summary="Read student by ID",
    description="Retrieve a specific student's details using their unique student ID."
)
def get_student_by_id(id: int):
    return student_controller.get_student_by_id(id)


# 4. Update Student
@router.put(
    "/{id}",
    response_model=Student,
    status_code=status.HTTP_200_OK,
    summary="Update student by ID",
    description="Update an existing student's information using their student ID."
)
def update_student(id: int, student: StudentUpdate):
    return student_controller.update_student(id, student)


# 5. Delete Student
@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete student by ID",
    description="Delete a student record from the system. Returns 204 No Content upon successful deletion."
)
def delete_student(id: int):
    student_controller.delete_student(id)
    return None
    
