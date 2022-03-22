# Messages Sender

<p align="center">
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>


Format and send a message following a template.

## Description
Message sender is a library which create a message to send from a python dictionnary and a Jinja template and send it by [the method of your choice](##Send methods available).

<img src=".doc/create_msg.svg" alt="pipeline" style="zoom:60%;" />


## Getting Started

### Dependencies
* python3.8+

### Installing
```bash
pip install messages-sender
```

### Use it

example:
```python
from messages-sender import MessageSender
credentials = {
    "SMTP": {
        "port": 465,
        "password": "your_mail_password",
        "sender_email": "your_mail",
    },
}
method = "smtp"
template = "templates/mail_template.jinja"
message = {
    "subject": "Test",
    "core": "The results of your analyse are available.",
    "results": {"link": "https://github.com/Ermite28/messages_sender", "label": "See the result"},
    "greetings": "Best regards,\nBenoît de Witte",
    "senders": {"info": "Ermite28, Belgium"},
}
MessageSender(credentials=credentials, method=method, template=template).send_message("your_email", message=message)

```



## TODO

- [V] Maybe rethink about the library interface?
- [ ] Make more example template
- [V] Handle mails attached files.
- [] Better error handling.
- [ ] Add unit test
- [V] should it handle file (config, template, message)? NO

## Send methods available

:white_check_mark: Telegram

:large_orange_diamond: SMTP (should handle attached files)

:red_circle: local

:red_circle: Signal

:red_circle: RSS

:red_circle: SMS

:red_circle: Discord bot

:red_circle: message_senders API (futur project)


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
