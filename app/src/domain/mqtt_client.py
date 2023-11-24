from abc import ABC, abstractmethod


class MQTTClient(ABC):
    @abstractmethod
    def publish_message_to_topic(self, topic: str, message: dict) -> None:
        ...

    @abstractmethod
    def subscribe_to_topic(self, topic: str) -> None:
        ...

    @abstractmethod
    def poll_message_from_subscribed_topic(self) -> dict:
        ...

    @abstractmethod
    def close_connection(self) -> None:
        ...
