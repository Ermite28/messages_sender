from pathlib import Path
import click
from senders import SenderFactory
from jinja2 import Template
from configparser import ConfigParser
import json


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
