from pydantic import BaseSettings


class Settings(BaseSettings):
    champions_json_path: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
