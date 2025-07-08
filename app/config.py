import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SENTRY_DSN = os.getenv("SENTRY_DSN")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./models.db")

settings = Settings()
