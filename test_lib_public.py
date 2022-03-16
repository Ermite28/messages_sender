from send_message import MessageSender

credentials = {
    "TELEGRAM": {"api_id": "ur_api_id", "api_hash": "ur_api_hash"},
    "SMTP": {
        "port": 465,
        "password": "ur_password",
        "sender_email": "ur_mail",
    },
}

method = "smtp"

template = "/home/ben/projects/messages_sender/templates/mail_template.jinja"

message = {
    "subject": "Test",
    "core": "Les resultats sont arrives.",
    "results": {"link": "https://github.com/Ermite28/messages_sender", "label": "Click for the code"},
    "greetings": "Bonne journée,",
    "senders": {"info": "Benoît de Witte, Belgium"},
}


MessageSender(credentials=credentials, method=method, template=template, message=message).send_message(
    "benoitdewitte28@gmail.com"
)
