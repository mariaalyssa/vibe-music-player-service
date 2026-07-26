from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Playlists endpoint", description="Returns a playlists-related welcome message")
def root() -> dict[str, str]:
    return {"message": "Welcome to Vibe Music Player Playlists Service"}

