from fastapi import HTTPException, status
from models.student_model import Student, StudentCreate, StudentUpdate

# In-memory storage for students (simulating local database with Python list of dictionaries)
students_db: list[dict] = [
    {
        "id": 1,
        "name": "Rahul Patel",
        "email": "rahul@example.com",
        "course": "B.Tech Computer Engineering",
        "semester": 5
    },
    {
        "id": 2,
        "name": "Priya Sharma",
        "email": "priya.sharma@example.com",
        "course": "B.Sc Information Technology",
        "semester": 3
    },
    {
        "id": 3,
        "name": "Amit Kumar",
        "email": "amit.k@example.com",
        "course": "BCA",
        "semester": 4
    },
    {
        "id": 4,
        "name": "Sneha Reddy",
        "email": "sneha.reddy@example.com",
        "course": "B.Tech Electronics",
        "semester": 6
    },
    {
        "id": 5,
        "name": "Vikram Singh",
        "email": "vikram.s@example.com",
        "course": "MCA",
        "semester": 2
    }
]

# Counter to generate unique student IDs
id_counter: int = len(students_db)


def create_student(student_data: StudentCreate) -> Student:
    """Create a new student record and store it in the in-memory list."""
    global id_counter
    id_counter += 1
    
    new_student = {
        "id": id_counter,
        "name": student_data.name,
        "email": student_data.email,
        "course": student_data.course,
        "semester": student_data.semester
    }
    students_db.append(new_student)
    return Student(**new_student)


def get_all_students() -> list[Student]:
    """Retrieve all student records from memory."""
    return [Student(**student) for student in students_db]


def get_student_by_id(student_id: int) -> Student:
    """Retrieve a single student record by its unique ID."""
    for student in students_db:
        if student["id"] == student_id:
            return Student(**student)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Student with ID {student_id} not found"
    )


def update_student(student_id: int, student_data: StudentUpdate) -> Student:
    """Update an existing student record by ID."""
    for student in students_db:
        if student["id"] == student_id:
            student["name"] = student_data.name
            student["email"] = student_data.email
            student["course"] = student_data.course
            student["semester"] = student_data.semester
            return Student(**student)
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Student with ID {student_id} not found"
    )


def delete_student(student_id: int) -> None:
    """Delete a student record by ID from memory."""
    for index, student in enumerate(students_db):
        if student["id"] == student_id:
            students_db.pop(index)
            return
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Student with ID {student_id} not found"
    )
