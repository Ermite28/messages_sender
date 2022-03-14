from schematics.models import Model
from schematics.types import IntType, StringType


class TelegramConfig(Model):
    # TODO: Be sure of theses values.
    api_id = IntType(max_value=99999999, min_value=10000000, required=True)
    api_hash = StringType(max_length=32, min_length=32)
