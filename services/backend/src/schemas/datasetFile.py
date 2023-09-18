from datetime import datetime
from typing import List
from bson.objectid import ObjectId
from pydantic import BaseModel
from .pyobject import PyObjectId

class DatasetFileBaseSchema(BaseModel):
    name: str
    path: str
    dataset: PyObjectId
    created_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CreateDatasetFileSchema(BaseModel):
    title: str
    dataset: PyObjectId


class DatasetFileResponse(DatasetFileBaseSchema):
    id: str
    dataset: PyObjectId
    created_at: datetime

class ListDatasetResponse(BaseModel):
    status: str
    results: int
    datasets: List[DatasetFileResponse]

class FilteredDatasetFileResponse(DatasetFileBaseSchema):
    id: str