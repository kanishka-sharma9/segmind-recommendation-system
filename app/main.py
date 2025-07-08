import sentry_sdk
from fastapi import FastAPI, HTTPException,APIRouter
# from .api import router
from .db import Base, engine
from .config import settings
from pydantic import BaseModel
from .recsys import get_recommendations
router=APIRouter()

class RecommendRequest(BaseModel):
    model_name: str

if settings.SENTRY_DSN:
    sentry_sdk.init(dsn=settings.SENTRY_DSN, traces_sample_rate=1.0)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Model Recommender")

@app.post('/recommend')
def recommend(request: RecommendRequest):
    try:
        recommendations = get_recommendations(request.model_name)
        return {"input": request.model_name, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
