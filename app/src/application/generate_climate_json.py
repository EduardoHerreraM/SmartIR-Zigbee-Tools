import decimal
from typing import Iterator


class GenerateClimateJson:
    def __init__(self):
        pass

    def __iterate_through_floats(
        self, minimum_float: float, maximum_float: float, step_size: float = 1.0
    ) -> Iterator[float]:
        number = minimum_float
        while number <= maximum_float:
            yield number
            number += step_size

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
        commands_list = {"off": ""}
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
                        commands_list[operation_mode][fan_mode][swing_mode][
                            str(int(temperature))
                        ] = ""

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
