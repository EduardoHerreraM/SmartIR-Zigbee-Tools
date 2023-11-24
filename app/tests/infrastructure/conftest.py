import pytest

from testcontainers.compose import DockerCompose

from src.infrastructure.mosquitto_mqtt_client import MosquittoMQTTClient


@pytest.fixture(scope="module", autouse=True)
def set_mosquitto_container() -> None:
    compose = DockerCompose(
        "app/tests/files", compose_file_name="mosquitto_docker_compose.yml", pull=True
    )
    with compose:
        _, __ = compose.get_logs()
        yield compose


@pytest.fixture()
def mosquitto_mqtt_client() -> MosquittoMQTTClient:
    client = MosquittoMQTTClient(broker_address="localhost", broker_port=1883)
    yield client
    client.close_connection()
