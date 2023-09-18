from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response
from pymongo.collection import ReturnDocument
from src.schemas.training_result import CreateTrainingResultSchema
from src.database import TrainingResult
from src.oauth2 import require_user
from src.serializers.trainingResultSerializers import trainingResultListEntity, populatedTrainingResultEntity, populatedTrainingResultListEntity
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

router = APIRouter()

@router.get('/')
def get_trainingResults(limit: int = 10, page: int = 1, search: str = '', user_id: str = Depends(require_user)):
    skip = (page - 1) * limit
    pipeline = [
        {'$match': {}},
        {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
        {'$skip': skip}, 
        {'$limit': limit}
    ]
    trainingResults = trainingResultListEntity(TrainingResult.aggregate(pipeline))
    return {'status': 'success', 'results': len(trainingResults), 'trainingResults': trainingResults}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_trainingResult(trainingResult: CreateTrainingResultSchema, user_id: str = Depends(require_user)):
    trainingResult_dict = {
        'note': trainingResult.note,
        'precision': trainingResult.precision,
        'recall': trainingResult.recall,
        'predicted_result' : trainingResult.predicted_result,
        'training_time': trainingResult.training_time,
        'user': ObjectId(user_id),
        'dataset': ObjectId(trainingResult.dataset),
        'training_model': ObjectId(trainingResult.training_model),
        'created_at':  datetime.utcnow(),
        'updated_at':  datetime.utcnow()
    }
    try:
        result = TrainingResult.insert_one(trainingResult_dict)
        pipeline = [
        {'$match': {}},
        {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
        ]

        new_trainingResult = trainingResultListEntity(TrainingResult.aggregate(pipeline))[0]
        # print(new_trainingResult)
        return new_trainingResult
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"trainingResult already exists")

@router.get('/{id}')
def get_trainingResult(id: str, user_id: str = Depends(require_user)):
    print(str)
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    pipeline = [
        {'$match': {'_id': ObjectId(id)}},
        {'$lookup': {'from': 'datasets', 'localField': 'dataset','foreignField': '_id', 'as': 'dataset'}},
        # {'$unwind': '$dataset'},
        { "$addFields": {
            "dataset": {
            "$arrayElemAt": [ "$dataset", 0 ]
            }
        }},
        {'$lookup': {'from': 'trainingModels', 'localField': 'training_model','foreignField': '_id', 'as': 'training_model'}},
        # {'$unwind': '$training_model'},
        { "$addFields": {
            "training_model": {
            "$arrayElemAt": [ "$training_model", 0 ]
            }
        }},
        {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
    ]
    db_cursor = TrainingResult.aggregate(pipeline)
    results = list(db_cursor)
    # print(results)
    # print(TrainingResult.find_one({'_id': ObjectId(id)}))
    if len(results) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No trainings with this id: {id} found")

    trainingResults = populatedTrainingResultListEntity(results)[0]
    return trainingResults


@router.delete('/{id}')
def delete_trainingResult(id: str, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    trainingResult = TrainingResult.find_one_and_delete({'_id': ObjectId(id)})
    if not trainingResult:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No trainingResult with this id: {id} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
