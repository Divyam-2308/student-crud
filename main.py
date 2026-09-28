from fastapi import FastAPI
from routes.student_routes import router as student_router

# Initialize the FastAPI application
app = FastAPI(
    title="Student CRUD API",
    description="A simple REST API for managing university student records using in-memory local storage.",
    version="1.0.0"
)

# Root endpoint
@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Student Management API. Visit /docs to view Swagger documentation."
    }

# Register student router
app.include_router(student_router)
