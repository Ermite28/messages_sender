from setuptools import find_packages, setup
from senders.__version__ import __version__ as version

setup(
    name="messages_sender",
    packages=find_packages(include=["messages_sender"]),
    version=version,
    description="Format and send a message following a template.",
    author="Ermite28",
    license="MIT",
    install_requires=["Telethon>=1.24.0"],
)
