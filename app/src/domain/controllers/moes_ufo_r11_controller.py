from src.domain.abstract_controller import AbstractController


class MOES_UFO_R11_Controller(AbstractController):
    def get_learning_mode_message(self) -> dict:
        return {"learn_ir_code": "ON"}

    def extract_code_from_message(self, message: dict) -> str:
        return message["learned_ir_code"]
