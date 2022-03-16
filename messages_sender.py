from senders import SenderFactory
from jinja2 import Template
from configparser import ConfigParser


class MessageSender:
    def __init__(self, credentials, method=None, template=None):
        self._set_credentials_parser(credentials)
        self._set_method(method)
        self._set_template(template)

    def _set_method(self, method):
        self._method = method

    def _set_template(self, template):
        if isinstance(template, Template):
            self._template = template
        else:
            raise Exception("{template} should be a jinja2 template.")

    def _set_credentials_parser(self, credentials):
        credentials_parser = ConfigParser()
        credentials_parser.read_dict(credentials)
        self._credentials_parser = credentials_parser

    def send_message(self, contact, message):
        SenderFactory.send(contact, self._template, message, self._credentials_parser, self._method)
