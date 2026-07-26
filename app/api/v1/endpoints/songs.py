from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Songs endpoint", description="Returns a songs-related welcome message")
def root() -> dict[str, str]:
    return {"message": "Welcome to Vibe Music Player Songs Service"}

