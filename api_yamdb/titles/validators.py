import datetime

from django.core.exceptions import ValidationError


def year_validator(value):
    if value < 1900 or value > datetime.datetime.now().year:
        raise ValidationError(
            ('%(value)s is not a correcrt year!'),
            params={'value': value},
        )
