import pytest

from src.application.generate_climate_json import GenerateClimateJson


@pytest.fixture
def generate_climate_json() -> GenerateClimateJson:
    return GenerateClimateJson()
