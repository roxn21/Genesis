from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

@router.post("/analyze/")
def analyze_sentiment(request: SentimentRequest):
    text = request.text.lower()
    
    if any(word in text for word in ["good", "happy", "great", "amazing"]):
        sentiment = "positive"
    elif any(word in text for word in ["bad", "sad", "terrible", "worst"]):
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return {"sentiment": sentiment}