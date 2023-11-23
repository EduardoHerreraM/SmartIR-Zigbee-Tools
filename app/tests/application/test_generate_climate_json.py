import json

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
    expected_output_file_path = "app/tests/files/correct_inputs_expected_output.json"
    with open(expected_output_file_path) as f:
        expected_output = json.load(f)

    generated_json = generate_climate_json(
        manufacturer=manufacturer,
        model=model,
        minimum_temperature=minimum_temperature,
        maximum_temperature=maximum_temperature,
        fan_modes=fan_modes,
        operation_modes=operation_modes,
        swing_modes=swing_modes,
    )

    assert generated_json == expected_output
