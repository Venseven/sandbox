from fastapi import APIRouter
import pandas as pd

router = APIRouter()
router2 = APIRouter()


DATABASE_FILE = "database/students.csv"

@router.get("/students") #decorators
def show_students():
    """JOB: Read the notebook and show every student."""
    df = pd.read_csv(DATABASE_FILE)
    return df.to_dict(orient="records")

@router.post("/students")
def add_student(name: str, grade: int):
    """JOB: Add one new student to the notebook."""
    df = pd.read_csv(DATABASE_FILE)
    next_id = len(df) + 1
    
    new_student = pd.DataFrame([{"id": next_id, "name": name, "grade": grade}])
    new_student.to_csv(DATABASE_FILE, mode='a', header=False, index=False)
        
    return {"message": "Student added!", "id": next_id, "name": name}

@router2.post("/math/add")
def add(a: int, b: int):
    return a + b


def subtract(a,b):
    return a - b