from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.routers import auth, user, dataset, datasetFile, trainingModel, trainingResult

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')
app.include_router(dataset.router, tags=['Datasets'], prefix='/api/datasets')
app.include_router(datasetFile.router, tags=['DatasetFiles'], prefix='/api/datasetFile')
app.include_router(trainingModel.router, tags=['TrainingModels'], prefix='/api/trainingModels')
app.include_router(trainingResult.router, tags=['TrainingResult'], prefix='/api/trainingResults')

@app.get("/")
def home():
    return "Hello, World!"