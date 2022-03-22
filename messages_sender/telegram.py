from telethon.sync import TelegramClient
from .senders import Senders


class SendByTelegram(Senders):
    def __init__(self, api_id=None, api_hash=None):
        self.api_id = api_id
        self.api_hash = api_hash

    def _send(self, contact, message, **kwargs):
        with TelegramClient("name", self.api_id, self.api_hash) as telegram_client:
            telegram_client.send_message(contact, message)
