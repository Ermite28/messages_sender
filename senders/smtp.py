from schematics.models import Model
from schematics.types import IntType, StringType
import smtplib, ssl
from .senders import Senders


class SendBySMTP(Senders):
    name = "smtp"

    @staticmethod
    def _set_credentials(config_parser):
        credentials = SMTPConfig()
        credentials.ports = config_parser.get("SMTP", "ports", fallback=465)
        credentials.password = config_parser.get("SMTP", "password")
        credentials.sender_email = config_parser.get("SMTP", "sender_email")
        credentials.validate()
        return credentials

    def _send(self, contact, formatted_message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.credentials.port, context=context) as server:
            server.login(self.credentials.sender_email, self.credentials.password)
            server.sendmail(self.credentials.sender_email, contact, formatted_message)


class SMTPConfig(Model):
    port = IntType(min_value=0, max_value=1023, default=465)
    password = StringType()
    sender_email = StringType()
