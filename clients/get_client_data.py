# Should be in db.
clients = {
    "Papy": {
        "Telegram": 101,
        "Mail": "benoitdewitte28@gmail.com",
        "API": {"routes": "/root/to/post", "authentification": {}},
    },
    "Manu": {
        "Telegram": 101,
        "Mail": "benoitdewitte28@gmail.com",
        "API": {"routes": "/root/to/post", "authentification": {}},
    },
}


class GetClientsData:
    @static
    def get_any(client_name, data_type="all"):
        if data_type == "all":
            return clients[client_name]
        try:
            return clients[client_name][data_type]
        except KeyError:
            raise (
                f"We don't have {data_type} informations for client {client_name}. \n"
                f"Make sure this client exists and have {data_type} informations."
            )
