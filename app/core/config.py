from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Doc_Classifier"

settings = Settings()