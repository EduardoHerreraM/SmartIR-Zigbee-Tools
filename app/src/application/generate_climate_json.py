class GenerateClimateJson:
    def __init__(self):
        pass

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
        return {
            "manufacturer": manufacturer,
            "supportedModels": [model],
            "commandsEncoding": "Raw",
            "supportedController": "MQTT",
            "minTemperature": minimum_temperature,
            "maxTemperature": maximum_temperature,
            "operationModes": operation_modes,
            "fanModes": fan_modes,
            "swingModes": swing_modes
        }
