from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Root endpoint", description="Returns a welcome message")
def root() -> dict[str, str]:
    return {"message": "Welcome to Vibe Music Player Auth Service"}


@router.get("/health-check", summary="Health check endpoint", description="Checks the health of the service")
def health_check() -> dict[str, str]:
    return {"message": "Health check passed"}