from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(title="Vibe Music Player Service")
app.include_router(api_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to Vibe Music Player Service"}


@app.get("/health-check")
def health_check() -> dict[str, str]:
    return {"message": "Welcome to Vibe Music Player Service"}
