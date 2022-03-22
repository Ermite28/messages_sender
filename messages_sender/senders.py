class Senders:
    def __init__(self):
        pass

    def send(self, contact, message, template=None, **kwargs):
        if template:
            message = self._apply_template(template, message)
        return self._send(contact, message, **kwargs)

    def _apply_template(self, template, message):
        return template.render(**message)

    def _send(self, contact, message, **kwargs):
        pass
