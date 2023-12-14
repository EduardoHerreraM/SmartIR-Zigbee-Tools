import json

from src.infrastructure.mosquitto_mqtt_client import MosquittoMQTTClient
from src.application.generate_climate_json import GenerateClimateJson
from src.domain.controllers.moes_ufo_r11_controller import MOES_UFO_R11_Controller
from settings import Settings


if __name__ == "__main__":
    settings = Settings(_env_file="properties.env")

    controller = MOES_UFO_R11_Controller(
        controller_read_code_topic=f"zigbee2mqtt/{settings.CONTROLLER_FRIENDLY_NAME}",
        controller_set_learning_topic=f"zigbee2mqtt/{settings.CONTROLLER_FRIENDLY_NAME}/set",
    )
    mqtt_client = MosquittoMQTTClient(
        broker_address=settings.BROKER_ADDRESS,
        broker_port=settings.BROKER_PORT,
        username=settings.USERNAME,
        password=settings.PASSWORD,
    )
    generate_climate_json = GenerateClimateJson(
        mqtt_client=mqtt_client, controller=controller
    )

    codes = generate_climate_json(
        manufacturer=settings.MANUFACTURER,
        model=settings.MODEL,
        minimum_temperature=settings.MINIMUM_TEMPERATURE,
        maximum_temperature=settings.MAXIMUM_TEMPERATURE,
        operation_modes=settings.OPERATION_MODES,
        fan_modes=settings.FAN_MODES,
        swing_modes=settings.SWING_MODES,
    )

    with open(f"{settings.MANUFACTURER}-{settings.MODEL}-codes.json", "w") as f:
        json.dump(codes, f, indent=4, default=str)
