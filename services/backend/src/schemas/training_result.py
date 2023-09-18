from datetime import datetime
from typing import List
from bson.objectid import ObjectId
from pydantic import BaseModel
from .pyobject import PyObjectId
from .user import FilteredUserResponse

class TrainingResultBaseSchema(BaseModel):
    note: str
    precision: int
    recall: int
    predicted_result: int
    training_time: int
    dataset: PyObjectId
    training_model: PyObjectId
    user: PyObjectId
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CreateTrainingResultSchema(BaseModel):
    note: str
    precision: int
    recall: int
    predicted_result: int
    training_time: int
    dataset: PyObjectId
    training_model: PyObjectId

class TrainingResultResponse(TrainingResultBaseSchema):
    id: str
    user: FilteredUserResponse
    created_at: datetime
    updated_at: datetime

class ListTrainingResultResponse(BaseModel):
    status: str
    results: int
    trainingResults: List[TrainingResultResponse]