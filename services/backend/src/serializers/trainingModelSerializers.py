from src.serializers.userSerializers import embeddedUserResponse

def embeddedTrainingResultResponse(trainingResult) -> dict:
    return {
        "id": str(trainingResult["_id"]),
        "note": trainingResult["note"],
        "precision": trainingResult["precision"],
        "recall": trainingResult["recall"],
        "predicted_result": trainingResult["predicted_result"],
        "training_time": trainingResult["training_time"],
        "created_at": trainingResult["created_at"],
    }

def embeddedTrainingResultListResponse(trainingModels) -> dict:
    return [embeddedTrainingResultResponse(trainingModel) for trainingModel in trainingModels]

def trainingModelEntity(trainingModel) -> dict:
    return {
        "id": str(trainingModel["_id"]),
        "description": trainingModel["description"],
        "train_test_split": trainingModel["train_test_split"],
        "dropout_ratio": trainingModel["dropout_ratio"],
        "layers_num": trainingModel["layers_num"],
        "user": embeddedUserResponse(trainingModel["user"]),
        "created_at": trainingModel["created_at"],
        "updated_at": trainingModel["updated_at"],
    }

def populatedTrainingModelEntity(trainingModel) -> dict:
    return {
        "id": str(trainingModel["_id"]),
        "description": trainingModel["description"],
        "train_test_split": trainingModel["train_test_split"],
        "dropout_ratio": trainingModel["dropout_ratio"],
        "layers_num": trainingModel["layers_num"],
        "training_results": embeddedTrainingResultListResponse(trainingModel["training_results"]),
        "user": embeddedUserResponse(trainingModel["user"]),
        "created_at": trainingModel["created_at"],
        "updated_at": trainingModel["updated_at"],
    }

def trainingModelListEntity(trainingModels) -> list:
    return [trainingModelEntity(trainingModel) for trainingModel in trainingModels]

def embeddedTrainingModelResponse(trainingModel) -> dict:
    return {
        "id": str(trainingModel["_id"]),
        "description": trainingModel["description"],
        "train_test_split": trainingModel["train_test_split"],
        "dropout_ratio": trainingModel["dropout_ratio"],
        "layers_num": trainingModel["layers_num"],
        "created_at": trainingModel["created_at"],
    }

def populatedTrainingModelListEntity(trainingModels) -> dict:
    return [populatedTrainingModelEntity(trainingModel) for trainingModel in trainingModels]

def embeddedTrainingModelResponseListEntity(trainingModels) -> dict:
    return [embeddedTrainingModelResponse(trainingModel) for trainingModel in trainingModels]