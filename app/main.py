from fastapi import FastAPI
from app.api.v1.endpoints import sentiment, health

app = FastAPI(
    title="AI-Based Sentiment Analysis API",
    description="A simple API to analyze sentiment of text inputs using FastAPI.",
    version="1.0.0"
)

# Include routers
app.include_router(sentiment.router, prefix="/v1", tags=["Sentiment Analysis"])

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running 🚀"}

