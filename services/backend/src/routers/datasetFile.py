from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response, Form
from fastapi import File, UploadFile
from pymongo.collection import ReturnDocument
from src.schemas.datasetFile import CreateDatasetFileSchema
from src.database import DatasetFile
from src.oauth2 import require_user
from src.serializers.datasetFileSerializers import datasetFileEntity, datasetFileListEntity
from pymongo.errors import DuplicateKeyError
from fastapi import File, UploadFile
from bson.objectid import ObjectId
from src.schemas.pyobject import PyObjectId
import os
import shutil
from starlette.responses import FileResponse

router = APIRouter()

@router.post('/upload')
def add_datasetFile(dataset: str = Form(...), file: UploadFile = File(...), user_id: str = Depends(require_user)):
    upload_dir = os.path.join(os.getcwd(), 'static/uploads/{}/{}'.format(user_id, dataset))
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    dest = os.path.join(upload_dir, file.filename)

    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    datasetFile_dict = {
        'path': dest,
        "name": file.filename,
        'dataset': ObjectId(dataset),
        'created_at':  datetime.utcnow()
    }

    try:
        result = DatasetFile.insert_one(datasetFile_dict)
        pipeline = [
            {'$match': {'_id': result.inserted_id}}
        ]
        new_datasetFile = datasetFileListEntity(DatasetFile.aggregate(pipeline))[0]
        return new_datasetFile
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"File already exists")

@router.get('/download')
def get_datasetFile(datasetFileId: str, user_id: str = Depends(require_user)):
    try:
        print(datasetFileId)
        datasetFile = DatasetFile.find_one({'_id': ObjectId(datasetFileId)})
        return FileResponse(datasetFile['path'], media_type='application/octet-stream')

    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"File not exists")