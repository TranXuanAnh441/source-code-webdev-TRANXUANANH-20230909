# NoCodeTrainer

Online AI training application.

## Project Building

```bash
$ docker-compose up -d --build
```
Or
```bash
$ docker-compose build
$ docker-compose up -d
```
The app frontend is available on http://localhost:8080
The app backend is available on http://localhost:5000 (swagger UI: http://localhost:5000/docs)

## Backend only

```bash
$ python -m venv venv

$ venv\Scripts\activate

$ pip install --upgrade pip

$ pip install -r requirements.txt

$ uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
```

## Frontend only 

If you build the frontend only, it is available on port http://localhost:8081

```bash
$ npm install

$ npm run serve

```

## File structure
```python
.
├── README.md
├── docker-compose.yml
└── services/
    ├── backend/
    │   ├── src/
    │   │   ├── routers # store the routes of the api
    │   │   │   ├── auth.py
    │   │   │   ├── dataset.py
    │   │   │   ├── datassetFile.py
    │   │   │   ├── trainingModel.py
    │   │   │   ├── trainingResult.py
    │   │   │   └── user.py
    │   │   ├── schemas / # store the schemas of the database
    │   │   │   ├── dataset.py
    │   │   │   ├── datasetFile.py
    │   │   │   ├── pyobject.py
    │   │   │   ├── training_model.py
    │   │   │   ├── training_result.py
    │   │   │   └── user.py
    │   │   ├── serializers/ # store the serializers for mongodb
    │   │   │   ├── datasetSerializers.py
    │   │   │   ├── datasetFileSerializers.py
    │   │   │   ├── trainingModelSerializers.py
    │   │   │   ├── trainingResultSerializers.py
    │   │   │   └── userSerializers.py
    │   │   ├── config.py
    │   │   ├── databasse.py
    │   │   ├── main.py
    │   │   ├── oauth2.py
    │   │   └── utils.py
    │   ├── static/
    │   │   └── uploads # store file uploaded by users
    │   └── .env # environment file for the backend
    ├── frontend/
    │   ├── node_modulles
    │   ├── public/
    │   │   ├── favicon.co
    │   │   └── index.html
    │   ├── src/
    │   │   ├── assets/
    │   │   │   ├── img/
    │   │   │   │   ├── ai-logo.png
    │   │   │   │   └── hero-img.png
    │   │   │   └── logo.png
    │   │   ├── components/ # UI components
    │   │   │   ├── HelloWorld.vue
    │   │   │   ├── NavBar.vue
    │   │   │   ├── Footer.vue
    │   │   │   ├── HeroImage.vue
    │   │   │   ├── DatasetListItem.vue
    │   │   │   └── ModelListItem.vue
    │   │   ├── routers/ # routing config
    │   │   │   └── index.js
    │   │   ├── store/ # store the state of the datas
    │   │   │   ├── modules/
    │   │   │   │   ├── datasets.js
    │   │   │   │   ├── models.js
    │   │   │   │   ├── trainings.js
    │   │   │   │   └── users.js
    │   │   │   └── index.js
    │   │   ├── views/ # pages of the frontend
    │   │   │   ├── Datasets/
    │   │   │   │   ├── CreateDatasetView.vue
    │   │   │   │   ├── DatasetListView.vue
    │   │   │   │   └── DatasetView.vue
    │   │   │   ├── Models/
    │   │   │   │   ├── CreateModelView.vue
    │   │   │   │   ├── ModelListView.vue
    │   │   │   │   └── ModelView.vue
    │   │   │   ├── Trainings/
    │   │   │   │   ├── TrainingView.vue
    │   │   │   │   └── TrainingListView.vue
    │   │   │   ├── Users/
    │   │   │   │   ├── LoginView.vue
    │   │   │   │   ├── ProfileView.vue
    │   │   │   │   └── RegisterView.vue
    │   │   │   ├── DashBoardView.vue
    │   │   │   ├── ErrorView.vue
    │   │   │   └── HomeView.vue
    │   │   └── App.vue
    │   └── main.js
    ├── .gitignore
    ├── Lable.config.js
    ├── Dockerfile
    ├── jsconfig.json
    ├── package.json
    └── vue.config.js
```