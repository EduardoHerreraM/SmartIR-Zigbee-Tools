from unittest.mock import Mock
import pytest

from src.application.generate_climate_json import GenerateClimateJson
from src.domain.abstract_controller import AbstractController
from src.domain.mqtt_client import MQTTClient


@pytest.fixture()
def controller() -> Mock:
    mock = Mock(spec=AbstractController)
    mock.controller_read_code_topic = ""
    mock.controller_set_learning_topic = ""
    return mock


@pytest.fixture()
def mqtt_client() -> Mock:
    return Mock(spec=MQTTClient)


@pytest.fixture()
def generate_climate_json(
    controller: AbstractController, mqtt_client: MQTTClient
) -> GenerateClimateJson:
    return GenerateClimateJson(mqtt_client=mqtt_client, controller=controller)
