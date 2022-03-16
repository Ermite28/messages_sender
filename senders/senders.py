from jinja2.exceptions import UndefinedError


class Senders:
    def __init__(self, credentials):
        self.credentials = self._set_credentials(credentials)

    def set_credentials(self, credentials):
        self._set_credentials(credentials)

    def send(self, contact, template, message):
        formatted_message = self._format_message(template, message)
        self._send(contact, formatted_message)

    def _format_message(self, template, message):
        try:
            return template.render(message=message)
        except UndefinedError as err:
            raise UndefinedError(f"Your template ask for keys with are not in your message.\n{err}")

    def _send(self):
        pass

    def _set_credentials(self):
        pass


class SenderFactory:
    @staticmethod
    def _get_sender(method_name):
        try:
            return [cls for cls in SenderFactory.get_available_senders() if cls.name == method_name][0]
        except IndexError:
            raise KeyError(f"{method_name} method is not implemented.")

    @staticmethod
    def get_available_senders():
        return [cls for cls in Senders.__subclasses__()]

    @staticmethod
    def send(contact, template, message, credentials, method):
        SenderFactory._get_sender(method)(credentials).send(contact, template, message)
