from pathlib import Path
from .text_format import TextFormat
from .message import Message


class MessageFactory:
    @staticmethod
    def select(input_file):
        file_format = Path(input_file).suffix
        if file_format == ".txt":
            return TextFormat(input_file)
        return Message(input_file)
