import pytest

from testcontainers.compose import DockerCompose

from src.infrastructure.mosquitto_mqtt_client import MosquittoMQTTClient


@pytest.fixture(scope="module", autouse=True)
def set_mosquitto_container() -> None:
    compose = DockerCompose(
        "app/tests/files", compose_file_name="mosquitto_docker_compose.yml", pull=True
    )
    with compose:
        compose.exec_in_container(
            service_name="mosquitto",
            command=[
                "mosquitto",
                "passwd",
                "-b",
                "/mosquitto/config/mosquitto.passwd",
                "test",
                "test",
            ],
        )
        _, __ = compose.get_logs()
        yield compose


@pytest.fixture()
def mosquitto_mqtt_client() -> MosquittoMQTTClient:
    client = MosquittoMQTTClient(
        broker_address="localhost", broker_port=1883, username="test", password="test"
    )
    yield client
    client.close_connection()
