from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    MONGO_INITDB_DATABASE: str

    MONGO_INITDB_ADMIN_USERNAME: str
    MONGO_INITDB_ADMIN_EMAIL: str
    MONGO_INITDB_ADMIN_PASSWORD: str
    
    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    CLIENT_ORIGIN: str

    class Config:
        env_file = './.env'

settings = Settings()