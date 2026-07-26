from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Users endpoint", description="Returns a users-related welcome message")
def root() -> dict[str, str]:
    return {"message": "Welcome to Vibe Music Player Users Service"}

