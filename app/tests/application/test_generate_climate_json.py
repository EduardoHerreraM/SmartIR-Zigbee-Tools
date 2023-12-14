import json
from unittest.mock import Mock

from src.application.generate_climate_json import GenerateClimateJson


def test_given_inputs_when_they_are_correct_then_the_output_is_as_expected(
    generate_climate_json: GenerateClimateJson, mqtt_client: Mock, controller: Mock
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
    mqtt_client.poll_message_from_subscribed_topic.return_value = {
        "learned_ir_code": "this_code_is_an_example"
    }
    controller.extract_code_from_message.side_effect = lambda message: message[
        "learned_ir_code"
    ]

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


def test_given_inputs_when_they_are_correct_then_the_call_count_of_learning_and_retrieving_codes_is_the_same(
    generate_climate_json: GenerateClimateJson, mqtt_client: Mock, controller: Mock
) -> None:
    manufacturer = "test_manufacturer"
    model = "test_model"
    minimum_temperature = 29.0
    maximum_temperature = 30.0
    operation_modes = ["cool"]
    fan_modes = ["auto"]
    swing_modes = ["off"]
    mqtt_client.poll_message_from_subscribed_topic.return_value = {
        "learned_ir_code": "this_code_is_an_example"
    }
    controller.extract_code_from_message.side_effect = lambda message: message[
        "learned_ir_code"
    ]

    generate_climate_json(
        manufacturer=manufacturer,
        model=model,
        minimum_temperature=minimum_temperature,
        maximum_temperature=maximum_temperature,
        fan_modes=fan_modes,
        operation_modes=operation_modes,
        swing_modes=swing_modes,
    )

    mqtt_client.publish_message_to_topic.assert_called()
    mqtt_client.poll_message_from_subscribed_topic.assert_called()
    controller.get_learning_mode_message.assert_called()
    controller.extract_code_from_message.assert_called()

    assert (
        len(
            set(
                [
                    mqtt_client.publish_message_to_topic.call_count,
                    mqtt_client.poll_message_from_subscribed_topic.call_count,
                    controller.get_learning_mode_message.call_count,
                    controller.extract_code_from_message.call_count,
                ]
            )
        )
        == 1
    )  # all are equal


def test_given_valid_inputs_when_mode_includes_auto_and_fan_includes_auto_and_another_then_the_another_fan_is_a_copy_of_auto(
    generate_climate_json: GenerateClimateJson, mqtt_client: Mock, controller: Mock
) -> None:
    manufacturer = "test_manufacturer"
    model = "test_model"
    minimum_temperature = 18.0
    maximum_temperature = 30.0
    operation_modes = ["auto", "cool"]
    fan_modes = ["auto", "low"]
    swing_modes = ["off", "on"]
    expected_output_file_path = (
        "app/tests/files/correct_inputs_with_auto_operation_expected_output.json"
    )
    with open(expected_output_file_path) as f:
        expected_output = json.load(f)
    mqtt_client.poll_message_from_subscribed_topic.return_value = {
        "learned_ir_code": "this_code_is_an_example"
    }
    controller.extract_code_from_message.side_effect = lambda message: message[
        "learned_ir_code"
    ]

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


def test_given_valid_inputs_when_mode_includes_dry_and_fan_includes_auto_and_another_then_the_another_fan_is_a_copy_of_auto(
    generate_climate_json: GenerateClimateJson, mqtt_client: Mock, controller: Mock
) -> None:
    manufacturer = "test_manufacturer"
    model = "test_model"
    minimum_temperature = 18.0
    maximum_temperature = 30.0
    operation_modes = ["dry", "cool"]
    fan_modes = ["auto", "low"]
    swing_modes = ["off", "on"]
    expected_output_file_path = (
        "app/tests/files/correct_inputs_with_dry_operation_expected_output.json"
    )
    with open(expected_output_file_path) as f:
        expected_output = json.load(f)
    mqtt_client.poll_message_from_subscribed_topic.return_value = {
        "learned_ir_code": "this_code_is_an_example"
    }
    controller.extract_code_from_message.side_effect = lambda message: message[
        "learned_ir_code"
    ]

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
