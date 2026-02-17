from fastapi import FastAPI
from app.recommender import JobRecommender
from app.schemas import RecommendationResponse, RecommendationRequest
from typing import List

app = FastAPI(title="Job Recommendation system")
recommender = JobRecommender()
@app.post("/recommend", response_model=List[RecommendationResponse])
def recommend(request: RecommendationRequest):
    return recommender.recommend(request.resume_text, request.top_k)


