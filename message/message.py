import logging


class Message:
    def __init__(self, input_file):
        self.input_file = input_file

    def for_telegram(self):
        logging.warning("input file format is unknow and can leads to undesired formating")
        with open(self.input_file, "r", encoding="UTF-8") as f:
            return "".join(f.readlines())

    def for_mail(self):
        logging.warning("input file format is unknow and can leads to undesired formating")
        with open(self.input_file, "r", encoding="UTF-8") as f:
            return "".join(f.readlines())

    def for_api(self):
        logging.warning("input file format is unknow and can leads to undesired formating")
        with open(self.input_file, "r", encoding="UTF-8") as f:
            return "".join(f.readlines())
