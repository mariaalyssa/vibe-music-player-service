from fastapi import APIRouter

from app.api.v1.endpoints import auth, playlists, songs, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(songs.router, prefix="/songs", tags=["songs"])
api_router.include_router(playlists.router, prefix="/playlists", tags=["playlists"])
