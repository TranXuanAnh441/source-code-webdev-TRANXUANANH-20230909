from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response
from pymongo.collection import ReturnDocument
from src.schemas.training_model import CreateTrainingModelSchema,  UpdateTrainingModelSchema
from src.database import TrainingModel
from src.oauth2 import require_user
from src.serializers.trainingModelSerializers import trainingModelEntity, trainingModelListEntity, populatedTrainingModelListEntity, populatedTrainingModelEntity
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

router = APIRouter()

@router.get('/')
def get_trainingModels(limit: int = 10, page: int = 1, search: str = '', user_id: str = Depends(require_user)):
    skip = (page - 1) * limit
    pipeline = [
        {'$match': {}},
        {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
        {'$skip': skip}, 
        {'$limit': limit}
    ]
    if len(search) > 0:
        pipeline.insert(0, 
            {'$match' : {'$text': {'$search': search}}},
        )
    trainingModels = trainingModelListEntity(TrainingModel.aggregate(pipeline))
    return {'status': 'success', 'results': len(trainingModels), 'trainingModels': trainingModels}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_trainingModel(trainingModel: CreateTrainingModelSchema, user_id: str = Depends(require_user)):
    trainingModel_dict = {
        'description': trainingModel.description,
        'dropout_ratio': trainingModel.dropout_ratio,
        'layers_num' : trainingModel.layers_num,
        'train_test_split': trainingModel.train_test_split,
        'user': ObjectId(user_id),
        'created_at':  datetime.utcnow(),
        'updated_at':  datetime.utcnow()
    }
    try:
        result = TrainingModel.insert_one(trainingModel_dict)
        pipeline = [
            {'$match': {'_id': result.inserted_id}},
            {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
            {'$unwind': '$user'},
        ]
        new_trainingModel = trainingModelListEntity(TrainingModel.aggregate(pipeline))[0]
        print(new_trainingModel)
        return new_trainingModel
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"trainingModel with title: '{trainingModel.title}' already exists")


@router.put('/{id}')
def update_trainingModel(id: str, payload: UpdateTrainingModelSchema, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    updated_trainingModel = TrainingModel.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': payload.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
    if not updated_trainingModel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No trainingModel with this id: {id} found')
    return trainingModelEntity(updated_trainingModel)


@router.get('/{id}')
def get_trainingModel(id: str, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    pipeline = [
        {'$match': {'_id': ObjectId(id)}},
        {'$lookup': {'from': 'trainingResults', 'localField': '_id', 'foreignField': 'training_model', 'as': 'training_results'}},
        {'$lookup': {'from': 'users', 'localField': 'user','foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
        # {'$lookup': {'from': 'datasets', 'localField': 'dataset',
        #              'foreignField': '_id', 'as': 'dataset'}},
    ]
    db_cursor = TrainingModel.aggregate(pipeline)
    results = list(db_cursor)

    if len(results) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No model with this id: {id} found")

    trainingModels = populatedTrainingModelListEntity(results)[0]
    return trainingModels


@router.delete('/{id}')
def delete_trainingModel(id: str, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    trainingModel = TrainingModel.find_one_and_delete({'_id': ObjectId(id)})
    if not trainingModel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No trainingModel with this id: {id} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
