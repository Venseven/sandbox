from fastapi import FastAPI
from routers import students

app = FastAPI()

app.include_router(students.router)
app.include_router(students.router2)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)