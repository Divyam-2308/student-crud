# FastAPI Student CRUD

This is a FastAPI-based RESTful API for a Student CRUD application.

## Project Structure
- `main.py`: Entry point for the FastAPI application.
- `models/`: Database models and Pydantic schemas.
- `routes/`: API route definitions.
- `controllers/`: Business logic and database operations.
- `requirements.txt`: Python dependencies.

## How to Run

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   fastapi dev main.py
   ```
5. Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation.
