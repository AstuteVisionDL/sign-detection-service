"""Settings of application"""
from enum import Enum
from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class ModeEnum(str, Enum):
    """
    Mode of application
    """

    TEST = "test"
    PRODUCTION = "prod"


class ApplicationSettings(BaseSettings):
    """
    Settings for application
    """

    mode: ModeEnum = Field(default=ModeEnum.TEST, alias="MODE")
    prob_threshold: float = Field(default=0.5, alias="YOLO_PROB_THRESHOLD")


load_dotenv()
settings = ApplicationSettings()
