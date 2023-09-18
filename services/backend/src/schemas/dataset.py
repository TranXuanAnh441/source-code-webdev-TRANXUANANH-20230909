from datetime import datetime
from typing import List
from bson.objectid import ObjectId
from pydantic import BaseModel
from .pyobject import PyObjectId
from .user import FilteredUserResponse

class DatasetBaseSchema(BaseModel):
    title: str
    description: str
    user: PyObjectId
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class CreateDatasetSchema(BaseModel):
    title: str
    description: str

class DatasetResponse(DatasetBaseSchema):
    id: str
    user: FilteredUserResponse
    created_at: datetime
    updated_at: datetime

class UpdateDatasetSchema(BaseModel):
    title: str | None = None
    description: str | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class ListDatasetResponse(BaseModel):
    status: str
    results: int
    datasets: List[DatasetResponse]

class FilteredDatasetResponse(DatasetBaseSchema):
    id: str