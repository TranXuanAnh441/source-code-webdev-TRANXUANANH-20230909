from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response
from pymongo.collection import ReturnDocument
from src.schemas.dataset import CreateDatasetSchema,  UpdateDatasetSchema
from src.database import Dataset
from src.oauth2 import require_user
from src.serializers.datasetSerializers import datasetEntity, datasetListEntity, populatedDatasetListEntity
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

router = APIRouter()

@router.get('/')
def get_datasets(limit: int = 10, page: int = 1, search: str = '', user_id: str = Depends(require_user)):
    skip = (page - 1) * limit

    pipeline = [
        {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
        {'$skip': skip}, 
        {'$limit': limit},
    ]
    if len(search) > 0:
        pipeline.insert(0, 
            {'$match' : {'$text': {'$search': search}}},
        )
    res = Dataset.aggregate(pipeline)
    datasets = datasetListEntity(res)
    return {'status': 'success', 'results': len(datasets), 'datasets': datasets}

@router.get('/search')
def search_by_titles(search_text):
    result = Dataset.find({"$text": {"$search": search_text}}).limit(10)
    print(result)
    return {'status': 'success'}

# @router.get('/user')
# def get_datasetsUser(limit: int = 10, page: int = 1, search: str = '', user_id: str = Depends(require_user)):
#     skip = (page - 1) * limit
#     pipeline = [
#         {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
#         {'$match': {'user._id': ObjectId(user_id)}},
#         {'$unwind': '$user'},
#     ]
#     res = datasetListEntity(Dataset.aggregate(pipeline))
#     return {'status': 'success', 'datasets': res}

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_dataset(dataset: CreateDatasetSchema, user_id: str = Depends(require_user)):
    dataset_dict = {
        'title': dataset.title,
        'description': dataset.description,
        'user': ObjectId(user_id),
        'created_at':  datetime.utcnow(),
        'updated_at':  datetime.utcnow()
    }
    try:
        result = Dataset.insert_one(dataset_dict)
        pipeline = [
            {'$match': {'_id': result.inserted_id}},
            {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
            {'$unwind': '$user'},
        ]
        new_dataset = datasetListEntity(Dataset.aggregate(pipeline))[0]
        return new_dataset
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Dataset with title: '{dataset.title}' already exists")


@router.put('/{id}')
def update_dataset(id: str, payload: UpdateDatasetSchema, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    updated_dataset = Dataset.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': payload.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
    if not updated_dataset:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No dataset with this id: {id} found')
    return datasetEntity(updated_dataset)


@router.get('/{id}')
def get_dataset(id: str, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    pipeline = [
        {'$match': {'_id': ObjectId(id)}},
        {'$lookup': {'from': 'datasetFiles', 'localField': '_id', 'foreignField': 'dataset', 'as': 'files'}},
        {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
    ]
    db_cursor = Dataset.aggregate(pipeline)
    results = list(db_cursor)

    if len(results) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No datase with this id: {id} found")

    datasets = populatedDatasetListEntity(results)[0]
    return datasets


@router.delete('/{id}')
def delete_dataset(id: str, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    dataset = Dataset.find_one_and_delete({'_id': ObjectId(id)})
    if not dataset:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No dataset with this id: {id} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
