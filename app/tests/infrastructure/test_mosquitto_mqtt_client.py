import pytest

from src.domain.exceptions import ConnectionNotEstablishedException
from src.infrastructure.mosquitto_mqtt_client import MosquittoMQTTClient


def test_given_a_valid_connection_when_message_is_published_to_topic_then_no_error_is_raised(
    mosquitto_mqtt_client: MosquittoMQTTClient,
) -> None:
    topic = "test_topic"
    message = {"this is": "a test message"}

    mosquitto_mqtt_client.publish_message_to_topic(topic=topic, message=message)


def test_given_a_valid_connection_when_a_message_is_published_to_a_subscribed_topic_then_the_message_is_retrieved(
    mosquitto_mqtt_client: MosquittoMQTTClient,
) -> None:
    topic = "test_topic"
    message = {"this is": "a different test message"}
    mosquitto_mqtt_client.subscribe_to_topic(topic=topic)
    mosquitto_mqtt_client.publish_message_to_topic(topic=topic, message=message)

    retrieved_message = mosquitto_mqtt_client.poll_message_from_subscribed_topic()

    assert retrieved_message == message


def test_given_an_invalid_connection_when_the_client_is_initialized_then_an_exception_is_raised() -> (
    None
):
    with pytest.raises(TimeoutError):
        MosquittoMQTTClient(
            broker_address="1.1.1.1",
            broker_port=1883,
        )


def test_given_an_invalid_connection_credentials_when_the_message_is_tried_to_sent_an_exception_is_raised() -> (
    None
):
    mosquitto_mqtt_client = MosquittoMQTTClient(
        broker_address="localhost",
        broker_port=1883,
        username="not-valid",
        password="not-valid",
    )
    topic = "test_topic"
    with pytest.raises(ConnectionNotEstablishedException):
        mosquitto_mqtt_client.subscribe_to_topic(topic=topic)
