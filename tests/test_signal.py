from messages_sender import SendByTelegram
from jinja2 import Template


class TestSignal:
    def test_no_template(self, monkeypatch):
        def mock_send(self, contact, message, **kwargs):
            return message

        monkeypatch.setattr(SendByTelegram, "_send", mock_send)
        assert "Hey" == SendByTelegram().send("contact", message="Hey")

    def test_template(self, monkeypatch):
        def mock_send(self, contact, message, **kwargs):
            return message

        template = Template("Hello {{ contact_name }}.")
        monkeypatch.setattr(SendByTelegram, "_send", mock_send)
        assert "Hello contact." == SendByTelegram().send(
            "contact", message={"contact_name": "contact"}, template=template
        )
