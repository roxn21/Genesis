from fastapi import APIRouter
from pydantic import BaseModel
from nltk.sentiment import SentimentIntensityAnalyzer

router = APIRouter()
sia = SentimentIntensityAnalyzer()

class SentimentRequest(BaseModel):
    text: str

@router.post("/analyze/")
def analyze_sentiment(request: SentimentRequest):
    sentiment_scores = sia.polarity_scores(request.text)
    
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return {"sentiment": sentiment, "scores": sentiment_scores}