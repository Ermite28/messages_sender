from .message import Message


class TextFormat(Message):
    def __init__(self, input_file):
        super().__init__(input_file)

    def for_telegram(self):
        with open(self.input_file, "r", encoding="utf8") as f:
            return "".join(f.readlines())
