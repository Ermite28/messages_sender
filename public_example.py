from messages_sender import MessageSender
from jinja2 import Template

credentials = {
    "SMTP": {
        "port": 465,
        "password": "ur_password",
        "sender_email": "ur_mail",
    },
}

method = "smtp"

with open("templates/mail_template.jinja", "r") as f:
    template = Template(f.read())

message = {
    "subject": "Results are there!",
    "core": "The results of your analyse are available.",
    "results": {"link": "https://github.com/Ermite28/messages_sender", "label": "See the result"},
    "greetings": "Best regards,\nBenoît de Witte",
    "senders": {"info": "Ermite28, Belgium"},
}


MessageSender(credentials=credentials, method=method, template=template).send_message("ur email", message=message)
