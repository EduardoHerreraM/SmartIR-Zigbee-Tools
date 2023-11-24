from abc import ABC, abstractmethod


class AbstractController(ABC):
    def __init__(
        self, controller_read_code_topic: str, controller_set_learning_topic: str
    ):
        self.controller_read_code_topic = controller_read_code_topic
        self.controller_set_learning_topic = controller_set_learning_topic

    @abstractmethod
    def get_learning_mode_message(self) -> dict:
        ...

    @abstractmethod
    def extract_code_from_message(self, message: dict) -> str:
        ...
