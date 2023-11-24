from abc import ABC, abstractmethod


class MQTTClient(ABC):
    @abstractmethod
    def publish_message_to_topic(self, topic: str, message: dict) -> None:
        ...

    @abstractmethod
    def poll_message_from_topic(self, topic: str) -> dict:
        ...
