import json
import queue

import paho.mqtt.client as mqtt

from src.domain.mqtt_client import MQTTClient
from src.domain.exceptions import ConnectionNotEstablishedException


class MosquittoMQTTClient(MQTTClient):
    def __init__(
        self,
        broker_address: str,
        broker_port: int,
        username: str = None,
        password: str = None,
    ):
        self.__broker_address = broker_address
        self.__broker_port = broker_port
        self.__client = mqtt.Client()

        if username and password:
            self.__client.username_pw_set(username=username, password=password)

        self.__client.on_message = self.__on_message
        self.__client.connect(host=self.__broker_address, port=self.__broker_port)
        self.__queue = queue.Queue()
        self.__client.loop_start()

    def __on_message(self, client, userdata, message) -> None:
        data = message.payload.decode("utf-8")
        self.__queue.put(json.loads(data))

    def subscribe_to_topic(self, topic: str) -> None:
        err, mid = self.__client.subscribe(topic=topic)
        if err != mqtt.MQTT_ERR_SUCCESS:
            raise ConnectionNotEstablishedException()

    def publish_message_to_topic(self, topic: str, message: dict) -> None:
        err, mid = self.__client.publish(topic=topic, payload=json.dumps(message))
        if err != mqtt.MQTT_ERR_SUCCESS:
            raise ConnectionNotEstablishedException()

    def poll_message_from_subscribed_topic(self) -> dict:
        data = self.__queue.get()
        return data

    def close_connection(self) -> None:
        self.__client.loop_stop()
        self.__client.disconnect()
