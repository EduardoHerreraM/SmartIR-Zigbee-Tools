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
