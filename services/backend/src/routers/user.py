from fastapi import APIRouter, Depends, Form
from bson.objectid import ObjectId
from src.serializers.userSerializers import userResponseEntity
from src.database import User
from .. import oauth2
from src.schemas.user import UserResponse
from fastapi import File, UploadFile
from fastapi.responses import FileResponse
# from src.schemas.user_history import UserHistoryReponseSchema

router = APIRouter()

@router.get('/me', response_model=UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}