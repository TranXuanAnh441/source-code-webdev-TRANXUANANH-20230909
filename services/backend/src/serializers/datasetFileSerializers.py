# from src.serializers.datasetSerializers import embeddedDatasetResponse

def datasetFileEntity(datasetFile) -> dict:
    return {
        "id": str(datasetFile["_id"]),
        "path": datasetFile["path"],
        "name": datasetFile["name"],
        "dataset": str(datasetFile["dataset"]),
        "created_at": datasetFile["created_at"],
    }

def datasetFileListEntity(datasetFiles) -> list:
    return [datasetFileEntity(datasetFile) for datasetFile in datasetFiles]

def embeddedDatasetFileResponse(datasetFile) -> dict:
    return {
        "id": str(datasetFile["_id"]),
        "path": datasetFile["path"],
        'name': datasetFile['name'],
        "created_at": datasetFile["created_at"]
    }

def embeddedDatasetFileListResponse(datasetFiles) -> dict:
    return [embeddedDatasetFileResponse(datasetFile) for datasetFile in datasetFiles]