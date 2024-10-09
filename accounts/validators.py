from django.core.exceptions import ValidationError
from django.utils.translation import ngettext


class MinimumLengthValidator:
    """
    Validate that the password is of a minimum length.
    """

    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "Zadané heslo je příliš krátké!",
                    "Zadané heslo je příliš krátké!",
                    self.min_length,
                ),
                code="password_too_short",
                params={"min_length": self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            "Your password must contain at least %(min_length)d character.",
            "Your password must contain at least %(min_length)d characters.",
            self.min_length,
        ) % {"min_length": self.min_length}
