from fastapi import FastAPI
from app.services.health_service import get_health

app = FastAPI()

@app.get("/health")
def health():
    return get_health()