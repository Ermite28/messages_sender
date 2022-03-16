from pathlib import Path
import click
from senders import SenderFactory
from jinja2 import Template
from configparser import ConfigParser
import json


class MessageSender:
    def __init__(self, credentials, method=None, template=None, message=None):
        self._set_credentials_parser(credentials)
        self._method = None
        if method:
            self._set_method(method)
        self._set_template(template)
        self.message = message

    def _set_method(self, method):
        if method not in [cls.name for cls in SenderFactory.get_available_senders()]:
            raise Exception(
                f"""{method} is not an available send method.
            Available methods are : {[cls.name for cls in SenderFactory.get_available_senders()]}"""
            )
        self._method = method

    def _set_template(self, template):  # handle if file or Template
        with open(template, "r") as f:
            template = Template(f.read())
        self._template = template

    def _set_credentials_parser(self, credentials):
        credentials_parser = ConfigParser()
        credentials_parser.read_dict(credentials)
        self._credentials_parser = credentials_parser

    def send_message(self, contact, message=None):
        if not message:
            message = self.message
        SenderFactory.send(contact, self._template, message, self._credentials_parser, self._method)


@click.command()
@click.option("--contact", help="client contact.")
@click.option("--message", help="File with the contents to send.", type=click.Path(exists=True))
@click.option("--template", help="Template to use", type=click.Path(exists=True))
@click.option("--method", help="Method to send message")
@click.option(
    "--credentials",
    help="File with credentials",
    default=Path(Path(__file__).resolve().parent, ".config.ini"),
    type=click.Path(exists=True),
)
def send(contact, message, template, method, credentials):
    with open(template, "r") as f:
        template = Template(f.read())
    credentials_parser = ConfigParser()
    credentials_parser.read(credentials)
    with open(message, "r") as f_message:
        message = json.load(f_message)
    SenderFactory.send(contact, template, message, credentials_parser, method)


def send_message(client, file, methods, config):
    if isinstance(client, str):
        client = [client]
    if isinstance(methods, str):
        methods = [methods]
    Senders.send(client, file, config, methods=methods)


if __name__ == "__main__":
    send()
