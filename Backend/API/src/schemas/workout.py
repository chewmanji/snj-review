import datetime

from pydantic import BaseModel, Field

from src.models.enums import TrainingType


class WorkoutBase(BaseModel):
    type: TrainingType | None = None
    notes: str | None = Field(max_length=1000)


class WorkoutCreate(WorkoutBase):
    user_id: int


class Workout(WorkoutBase):
    id: int
    workout_date: datetime.date

    class Config:
        from_attributes = True


class WorkoutUpdate(BaseModel):
    id: int
    notes: str | None = Field(max_length=1000)
    workout_date: datetime.date | None = None
    type: TrainingType | None = None

    class Config:
        from_attributes = True