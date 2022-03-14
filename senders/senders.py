from clients import GetClientsData
from message import MessageFactory
from .telegram import SendByTelegram


class Senders:
    @staticmethod
    def send(clients, message_file, config, methods):
        if "telegram" in methods:
            sender = SendByTelegram(config)
            for client in clients:
                sender.send_message(GetClientsData().get_telegram(client), MessageFactory.select(message_file).for_telegram())
