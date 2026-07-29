"""Song service implementation."""

from typing import Optional

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


def get_song_by_id(song_id: int) -> Optional[dict[str, object]]:
    """Return a song by its ID from the database."""
    query = text(
        "SELECT id, title, artist, album, genre, duration, audio_url, cover_url, created_at FROM songs WHERE id = :song_id"
    )
    with engine.connect() as conn:
        result = conn.execute(query, {"song_id": song_id})
        row = result.mappings().first()
        return dict(row) if row else None