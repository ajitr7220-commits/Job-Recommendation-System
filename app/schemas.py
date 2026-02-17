from pydantic import BaseModel

class RecommendationResponse(BaseModel):
    title: str
    description: str
    jobrequirements: str


class RecommendationRequest(BaseModel):
    resume_text: str
    top_k: int = 5
    