
from fastapi import FastAPI

app = FastAPI(
    title="DeployDeck API",
    description="Self-service cloud deployment platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to DeployDeck!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "DeployDeck API"
    }
