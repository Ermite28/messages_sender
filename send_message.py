from pathlib import Path
import click
from senders import Senders


@click.command()
@click.option("--client", help="Client to send message.", multiple=True)
@click.option("--file", help="File with the contents to send.", type=click.Path(exists=True))
@click.option("--methods", multiple=True, help="Way to send message")
@click.option(
    "--config",
    help="File with credentials",
    default=Path(Path(__file__).resolve().parent, ".config.ini"),
    type=click.Path(exists=True),
)
def send(client, file, methods, config):
    Senders.send(client, file, config, methods=methods)

def send_message(client, file, methods, config):
    if isinstance(client, str):
        client = [client]
    if isinstance(methods, str):
        methods = [methods]
    Senders.send(client, file, config, methods=methods)


if __name__ == "__main__":
    send()
