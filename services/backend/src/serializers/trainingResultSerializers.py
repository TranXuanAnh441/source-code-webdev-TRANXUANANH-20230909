from src.serializers.trainingModelSerializers import embeddedTrainingModelResponse, trainingModelEntity
from src.serializers.userSerializers import embeddedUserResponse
from src.serializers.datasetSerializers import embeddedDatasetResponse, datasetEntity

def trainingResultEntity(trainingResult) -> dict:
    return {
        "id": str(trainingResult["_id"]),
        "note": trainingResult["note"],
        "precision": trainingResult["precision"],
        "recall": trainingResult["recall"],
        "predicted_result": trainingResult["predicted_result"],
        "training_time": trainingResult["training_time"],
        "user": embeddedUserResponse(trainingResult["user"]),
        "dataset": str(trainingResult["dataset"]),
        "training_model": str(trainingResult["training_model"]),
        "created_at": trainingResult["created_at"],
        "updated_at": trainingResult["updated_at"],
    }

def populatedTrainingResultEntity(trainingResult) -> dict:
    return {
        "id": str(trainingResult["_id"]),
        "note": trainingResult["note"],
        "precision": trainingResult["precision"],
        "recall": trainingResult["recall"],
        "predicted_result": trainingResult["predicted_result"],
        "training_time": trainingResult["training_time"],
        "dataset": embeddedDatasetResponse(trainingResult["dataset"]),
        "training_model": embeddedTrainingModelResponse(trainingResult["training_model"]),
        "user": embeddedUserResponse(trainingResult["user"]),
        "created_at": trainingResult["created_at"],
        "updated_at": trainingResult["updated_at"],
    }

def trainingResultListEntity(trainingResults) -> list:
    return [trainingResultEntity(trainingResult) for trainingResult in trainingResults]

def embeddedTrainingResultResponse(trainingResult) -> dict:
    return {
        "id": str(trainingResult["_id"]),
        "note": trainingResult["note"],
        "precision": trainingResult["precision"],
        "recall": trainingResult["recall"],
        "predicted_result": trainingResult["predicted_result"],
        "training_time": trainingResult["training_time"],
        "created_at": trainingResult["created_at"],
        "updated_at": trainingResult["updated_at"],
    }

def populatedTrainingResultListEntity(trainingResults) -> dict:
    return [populatedTrainingResultEntity(trainingResult) for trainingResult in trainingResults]

def embeddedTrainingResultResponseListEntity(trainingResults) -> dict:
    return [embeddedTrainingResultResponse(trainingResult) for trainingResult in trainingResults]