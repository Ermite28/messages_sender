import smtplib, ssl
from configparser import ConfigParser
from .smtp_config import SMTPConfig

class SendBySMTP:
    def __init__(self, config):
        self.credentials = self._set_credentials(config)
        self.context = ssl.create_default_context()

    @staticmethod
    def _set_credentials(config):
        config_parser = ConfigParser()
        if isinstance(config, dict):
            config_parser.read_dict(config)
        else:
            config_parser.read(config)
        credentials = SMTPConfig()
        credentials.ports = config_parser.get("SMTP", "ports", fallback=465)
        credentials.password = config_parser.get("SMTP", "password")
        credentials.sender_email = config_parser.get("SMTP", "sender_email")
        credentials.validate()
        return credentials

    def send_message(self, client, message):
        with smtplib.SMTP_SSL('smtp.gmail.com', self.credentials.port, context=self.context) as server:
            server.login(self.credentials.sender_email, self.credentials.password)
            server.sendmail(self.credentials.sender_email, client, message)



