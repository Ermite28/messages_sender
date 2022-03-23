from messages_sender import SendBySMTP
from jinja2 import Template


class TestSignal:
    def test_no_template(self, monkeypatch):
        def mock_send(self, contact, message, **kwargs):
            print(contact, message)
            return message

        monkeypatch.setattr(SendBySMTP, "_send", mock_send)
        assert "Hey" == SendBySMTP().send("contact", message="Hey")

    def test_template(self, monkeypatch):
        def mock_send(self, contact, message, **kwargs):
            return message

        template = Template("Hello {{ contact_name }}.")
        monkeypatch.setattr(SendBySMTP, "_send", mock_send)
        assert 323 == len(SendBySMTP().send("contact", message={"contact_name": "contact"}, template=template))
        assert "Hello contact." in SendBySMTP().send("contact", message={"contact_name": "contact"}, template=template)
