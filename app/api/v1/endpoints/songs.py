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

@router.get("/{song_id}", summary="Get a song by ID", description="Returns a song by its ID from the database")
def get_song(song_id: int):
    song = song_service.get_song_by_id(song_id)
    if song is None:
        return {"error": "Song not found"}
    return song
