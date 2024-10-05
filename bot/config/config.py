from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    REF_ID: str = ''

    AUTO_FARM: bool = True
    AUTO_QUESTS: bool = True

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [0, 15]

    FAKE_USERAGENT: bool = False
    ERRORS_BEFORE_STOP: int = 3

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
