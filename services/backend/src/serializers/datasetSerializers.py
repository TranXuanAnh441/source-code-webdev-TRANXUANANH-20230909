from src.serializers.userSerializers import embeddedUserResponse
from src.serializers.datasetFileSerializers import embeddedDatasetFileListResponse

def datasetEntity(dataset) -> dict:
    return {
        "id": str(dataset["_id"]),
        "title": dataset["title"],
        "description": dataset["description"],
        "user": embeddedUserResponse(dataset['user']),
        "created_at": dataset["created_at"],
        "updated_at": dataset["updated_at"]
    }

def populatedDatasetEntity(dataset) -> dict:
    return {
        "id": str(dataset["_id"]),
        "title": dataset["title"],
        "description": dataset["description"],
        'user': embeddedUserResponse(dataset['user']),
        'files': embeddedDatasetFileListResponse(dataset['files']),
        "created_at": dataset["created_at"],
        "updated_at": dataset["updated_at"]
    }

def datasetListEntity(datasets) -> list:
    return [datasetEntity(dataset) for dataset in datasets]

def populatedDatasetListEntity(datasets) -> list:
    return [populatedDatasetEntity(dataset) for dataset in datasets]

def embeddedDatasetResponse(dataset) -> dict:
    return {
        "id": str(dataset["_id"]),
        "title": dataset["title"],
        "description": dataset["description"],
        "created_at": dataset["created_at"],
    }

def embeddedDatasetResponseListEntity(datasets) -> dict:
    return [embeddedDatasetResponse(dataset) for dataset in datasets]