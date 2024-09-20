from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.core.database import Base, engine
from src.routers import (
    user,
    exercise,
    workout_exercise,
    workout,
    set
)

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user.router)
app.include_router(exercise.router)
app.include_router(workout_exercise.router)
app.include_router(workout.router)
app.include_router(set.router)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return "Hello wurld"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)