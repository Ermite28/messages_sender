from schematics.models import Model
from schematics.types import IntType, StringType
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
        formatted_message["From"] = self.credentials.sender_email
        formatted_message["To"] = contact
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.credentials.port, context=context) as server:
            server.login(self.credentials.sender_email, self.credentials.password)
            server.sendmail(self.credentials.sender_email, contact, formatted_message.as_string())

    def _format_message(self, template, message):
        mail = MIMEMultipart("alternative")
        if "subject" in message:
            mail["Subject"] = message["subject"]
        text_part = message["core"]
        html_part = super()._format_message(template, message)
        part1 = MIMEText(text_part, "plain")
        part2 = MIMEText(html_part, "html")
        mail.attach(part1)
        mail.attach(part2)
        return mail


class SMTPConfig(Model):
    port = IntType(min_value=0, max_value=1023, default=465)
    password = StringType()
    sender_email = StringType()
