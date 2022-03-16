from schematics.models import Model
from schematics.types import IntType, StringType
from telethon.sync import TelegramClient
from .senders import Senders


class SendByTelegram(Senders):
    name = "telegram"

    @staticmethod
    def _set_credentials(config_parser):
        credentials = TelegramConfig()
        credentials.api_id = config_parser.get("TELEGRAM", "api_id")
        credentials.api_hash = config_parser.get("TELEGRAM", "api_hash")
        credentials.validate()
        return credentials

    def _send(self, contact, formatted_message):
        with TelegramClient("name", self.credentials.api_id, self.credentials.api_hash) as telegram_client:
            telegram_client.send_message(contact, formatted_message)


class TelegramConfig(Model):
    api_id = IntType(max_value=99999999, min_value=10000000, required=True)
    api_hash = StringType(max_length=32, min_length=32)
