# Should be in db.
clients = {
    "Benoit": {
        "Telegram": "me",
        "Mail": "benoitdewitte28@gmail.com",
        "API": {"routes": "/root/to/post", "authentification": {}},
    },
    "An": {
        "Telegram": "An",
        "Mail": "An",
        "API": {"routes": "/root/to/post", "authentification": {}},
    },
}


class GetClientsData:
    @staticmethod
    def get_any(client_name, data_type="all"):
        if data_type == "all":
            return clients[client_name]
        try:
            return clients[client_name][data_type]
        except KeyError:
            raise KeyError(
                f"We don't have {data_type} informations for client {client_name}. \n"
                f"Make sure this client exists and have {data_type} informations."
            )

    def get_telegram(self, client_name):
        return self.get_any(client_name, data_type="Telegram")
