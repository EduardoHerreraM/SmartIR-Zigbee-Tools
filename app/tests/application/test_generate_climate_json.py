from src.application.generate_climate_json import GenerateClimateJson


def test_given_inputs_when_they_are_correct_then_the_output_is_as_expected(
    generate_climate_json: GenerateClimateJson,
) -> None:
    manufacturer = "test_manufacturer"
    model = "test_model"
    minimum_temperature = 18.0
    maximum_temperature = 30.0
    operation_modes = ["cool", "heat"]
    fan_modes = ["auto", "low"]
    swing_modes = ["off", "on"]

    generated_json = generate_climate_json(
        manufacturer=manufacturer,
        model=model,
        minimum_temperature=minimum_temperature,
        maximum_temperature=maximum_temperature,
        fan_modes=fan_modes,
        operation_modes=operation_modes,
        swing_modes=swing_modes,
    )

    assert generated_json
    assert generated_json["manufacturer"] == manufacturer
    assert generated_json["supportedModels"] == [model]
    assert generated_json["commandsEncoding"] == "Raw"
    assert generated_json["supportedController"] == "MQTT"
    assert generated_json["minTemperature"] == minimum_temperature
    assert generated_json["maxTemperature"] == maximum_temperature
    assert generated_json["operationModes"] == operation_modes
    assert generated_json["fanModes"] == fan_modes
    assert generated_json["swingModes"] == swing_modes
