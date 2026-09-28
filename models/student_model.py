from pydantic import BaseModel, Field

# Base model containing common fields for a student
class StudentBase(BaseModel):
    name: str = Field(..., min_length=1, description="Full name of the student")
    email: str = Field(..., min_length=3, description="Email address of the student")
    course: str = Field(..., min_length=1, description="Course or program name")
    semester: int = Field(..., ge=1, le=12, description="Current semester number (1 to 12)")

# Model used when creating a student (ID is assigned automatically)
class StudentCreate(StudentBase):
    pass

# Model used when updating an existing student
class StudentUpdate(StudentBase):
    pass

# Model representing a student returned to the client (includes generated ID)
class Student(StudentBase):
    id: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Rahul Patel",
                "email": "rahul@example.com",
                "course": "B.Tech Computer Engineering",
                "semester": 5
            }
        }
