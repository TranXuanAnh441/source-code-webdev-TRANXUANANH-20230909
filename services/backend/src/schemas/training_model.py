from datetime import datetime
from typing import List
from bson.objectid import ObjectId
from pydantic import BaseModel
from .pyobject import PyObjectId
from .dataset import FilteredDatasetResponse
from .user import FilteredUserResponse

class TrainingModelBaseSchema(BaseModel):
    description: str
    train_test_split: int
    dropout_ratio: int
    layers_num: int
    user: PyObjectId
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CreateTrainingModelSchema(BaseModel):
    description: str
    train_test_split: int
    dropout_ratio: int
    layers_num: int

class TrainingModelResponse(TrainingModelBaseSchema):
    id: str
    user: FilteredUserResponse
    created_at: datetime
    updated_at: datetime


class UpdateTrainingModelSchema(BaseModel):
    description: str | None = None
    train_test_split: int | None = None
    dropout_ratio: int | None = None
    layers_num: int | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ListTrainingModelResponse(BaseModel):
    status: str
    results: int
    trainingModels: List[TrainingModelResponse]

class FilteredTrainingModelResponse(TrainingModelBaseSchema):
    id: str