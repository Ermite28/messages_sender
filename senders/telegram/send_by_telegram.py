from configparser import ConfigParser
from telethon.sync import TelegramClient
from .telegram_config import TelegramConfig


class SendByTelegram:
    def __init__(self, config):
        self.credentials = self._set_credentials(config)

    @staticmethod
    def _set_credentials(config):
        config_parser = ConfigParser()
        if isinstance(config, dict):
            config_parser.read_dict(config)
        else:
            config_parser.read(config)
        credentials = TelegramConfig()
        credentials.api_id = config_parser.get("TELEGRAM", "api_id")
        credentials.api_hash = config_parser.get("TELEGRAM", "api_hash")
        credentials.validate()
        return credentials

    def send_message(self, client, message):
        with TelegramClient("name", self.credentials.api_id, self.credentials.api_hash) as telegram_client:
            telegram_client.send_message(client, message)
