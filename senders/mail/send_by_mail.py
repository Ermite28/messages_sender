from .smtp import SendBySMTP


class SendByMail():
    def __init__(self, config):
        self.config = config

    def send_message(self, client, message):
        if True: # TODO find a way to determine the protocol.
            SendBySMTP(self.config).send_message(client, message)