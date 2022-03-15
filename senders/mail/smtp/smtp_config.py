from schematics.models import Model
from schematics.types import IntType, StringType


class SMTPConfig(Model):
    port = IntType(min_value=0, max_value=1023, default=465)
    password = StringType()
    sender_email = StringType() # TODO: Change for emailType

