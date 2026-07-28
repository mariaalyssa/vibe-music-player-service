from fastapi import APIRouter

from app.services import song_service

router = APIRouter()


@router.get("/", summary="Songs endpoint", description="Returns a songs-related welcome message")
def root() -> dict[str, str]:
    return {"message": "Welcome to Vibe Music Player Songs Service"}


@router.get("/all", summary="Get all songs", description="Returns all songs from the database")
def get_songs():
    songs = song_service.get_all_songs()
    return songs

