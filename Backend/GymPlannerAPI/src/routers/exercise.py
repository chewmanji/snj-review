from fastapi import APIRouter, Depends, HTTPException, Path, Query

import src.crud.exercise
import src.schemas.exercise
from src.core.dependencies import get_db
from src.core import crud
from src.core import schemas
from sqlalchemy.orm import Session
from typing import Annotated

router = APIRouter(prefix="/exercises", tags=["Exercise"])


@router.get("", response_model=list[src.schemas.exercise.Exercise])
async def get_exercises(skip: Annotated[int, Query(ge=0)] = 0, limit: Annotated[int, Query(ge=0)] = 50,
                        db: Session = Depends(get_db)):
    return src.crud.exercise.get_exercises(db, skip=skip, limit=limit)


@router.get("/{exercise_id}", response_model=src.schemas.exercise.Exercise)
async def get_exercise(exercise_id: Annotated[int, Path(title="Exercise ID to get", gt=0)],
                       db: Session = Depends(get_db)):
    exercise = src.crud.exercise.get_exercise_by_id(db, exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise
