"""Song service implementation."""

from sqlalchemy import text

from app.database.session import engine


def get_all_songs() -> list[dict[str, object]]:
    """Return all songs from the database."""
    query = text(
        "SELECT id, title, artist, album, genre, duration, audio_url, cover_url, created_at FROM songs"
    )
    with engine.connect() as conn:
        result = conn.execute(query)
        return [dict(row) for row in result.mappings()]
