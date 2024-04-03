from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str = ""
    postgres_password: str = ""
    postgres_db: str = ""
    postgres_host: str = ""
    database_type: str = ""
    database_port: int = 5432
    jwt_secret_key: str = ""
    access_token_expire_minutes: int = 30
    hashing_algorithm: str = "HS256"
    modbus_tcp_host: str = ""
    modbus_tcp_port1: int = 503
    modbus_tcp_port2: int = 504

    # The Config class is used just for Pydantic configuration
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings():
    return Settings()
