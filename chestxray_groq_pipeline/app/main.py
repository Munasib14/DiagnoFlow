from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router

app = FastAPI(
    title="Chest X-ray Groq Pipeline",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "running"}
