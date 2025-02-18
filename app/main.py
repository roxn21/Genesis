from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")

def root():
    return {"msg" : "Sentiment Analysis API is running 🚀"}