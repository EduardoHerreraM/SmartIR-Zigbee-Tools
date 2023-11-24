from typing import Iterator

from src.domain.mqtt_client import MQTTClient
from src.domain.abstract_controller import AbstractController


class GenerateClimateJson:
    def __init__(self, mqtt_client: MQTTClient, controller: AbstractController):
        self.__mqtt_client = mqtt_client
        self.__controller = controller

    def __iterate_through_floats(
        self, minimum_float: float, maximum_float: float, step_size: float = 1.0
    ) -> Iterator[float]:
        number = minimum_float
        while number <= maximum_float:
            yield number
            number += step_size

    def __set_controller_to_learning_mode(self) -> None:
        self.__mqtt_client.publish_message_to_topic(
            topic=self.__controller.controller_set_learning_topic,
            message=self.__controller.get_learning_mode_message(),
        )

    def __get_controller_learnt_code(self) -> str:
        print("Setting the controller to learning mode...")
        controller_message = self.__mqtt_client.poll_message_from_topic(
            topic=self.__controller.controller_read_code_topic
        )
        return self.__controller.extract_code_from_message(message=controller_message)

    def __call__(
        self,
        manufacturer: str,
        model: str,
        minimum_temperature: float,
        maximum_temperature: float,
        operation_modes: list[str],
        fan_modes: list[str],
        swing_modes: list[str],
    ) -> dict[str : float | str]:
        self.__set_controller_to_learning_mode()

        print("Set the device to `off` mode")
        commands_list = {"off": self.__get_controller_learnt_code()}
        for operation_mode in operation_modes:
            commands_list[operation_mode] = {}
            for fan_mode in fan_modes:
                commands_list[operation_mode][fan_mode] = {}
                for swing_mode in swing_modes:
                    commands_list[operation_mode][fan_mode][swing_mode] = {}
                    for temperature in self.__iterate_through_floats(
                        minimum_float=minimum_temperature,
                        maximum_float=maximum_temperature,
                    ):
                        self.__set_controller_to_learning_mode()
                        print(
                            f"Set the controller to the following modes:\t"
                            f"operation={operation_mode}\t"
                            f"fan={fan_mode}\t"
                            f"swing={swing_mode}\t"
                            f"temperature={temperature}"
                        )
                        commands_list[operation_mode][fan_mode][swing_mode][
                            str(int(temperature))
                        ] = self.__get_controller_learnt_code()

        print("All needed codes learnt.")

        return {
            "manufacturer": manufacturer,
            "supportedModels": [model],
            "commandsEncoding": "Raw",
            "supportedController": "MQTT",
            "minTemperature": minimum_temperature,
            "maxTemperature": maximum_temperature,
            "operationModes": operation_modes,
            "fanModes": fan_modes,
            "swingModes": swing_modes,
            "commands": commands_list,
        }
