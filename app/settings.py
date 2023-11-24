from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BROKER_ADDRESS: str = Field()
    BROKER_PORT: int = Field()
    USERNAME: str = Field(default=None)
    PASSWORD: str = Field(default=None)
    CONTROLLER_FRIENDLY_NAME: str = Field(...)
    MANUFACTURER:  str = Field(...)
    MODEL:  str = Field(...)
    MINIMUM_TEMPERATURE:  float = Field(...)
    MAXIMUM_TEMPERATURE:  float = Field(...)
    OPERATION_MODES:  list[str] = Field(...)
    FAN_MODES:  list[str] = Field(...)
    SWING_MODES:  list[str] = Field(...)
