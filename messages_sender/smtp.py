import smtplib, ssl
from pathlib import Path
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from .senders import Senders


class SendBySMTP(Senders):
    def __init__(self, sender_email=None, sender_password=None, port=465):
        self.port = port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send(self, contact, message, template=None, **kwargs):  # Refactor
        if template:
            message = self._apply_template(template, message)
            message = self._create_mail(contact, message, **kwargs)
        return self._send(contact, message, **kwargs)

    def _create_mail(self, contact, message, subject=None, simple_form=None, attached_files=None):
        mail = MIMEMultipart("alternative")
        mail["Subject"] = subject
        mail["From"] = self.sender_email
        mail["To"] = contact
        if simple_form:
            text_part = simple_form
            part1 = MIMEText(text_part, "plain")
            mail.attach(part1)
        html_part = message
        part2 = MIMEText(html_part, "html")
        mail.attach(part2)
        if attached_files:
            for attached_files in self._get_attached_files(message["attached_files"]):
                mail.attach(attached_files)
        return mail.as_string()

    def _send(self, contact, mail, **kwargs):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, contact, mail)

    def _get_attached_files(self, files):
        attached_files = []
        for f in files:
            with open(f, "rb") as attachment:
                part = MIMEBase("application", "octet_strem")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {Path(f).name}",
            )
            attached_files.append(part)
        return attached_files
