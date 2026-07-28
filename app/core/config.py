from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_host: Optional[str] = None
    database_port: Optional[int] = None
    database_name: Optional[str] = None
    database_user: Optional[str] = None
    database_password: Optional[str] = None
    database_url: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def resolved_database_url(self) -> str:
        if self.database_url:
            return self.database_url

        if not all(
            [
                self.database_host,
                self.database_port,
                self.database_name,
                self.database_user,
                self.database_password,
            ]
        ):
            raise ValueError(
                "DATABASE_URL or all database settings must be provided."
            )

        return (
            f"postgresql://{self.database_user}:"
            f"{self.database_password}@"
            f"{self.database_host}:"
            f"{self.database_port}/"
            f"{self.database_name}"
        )

settings = Settings()