from django import template

register = template.Library()

@register.filter
def custom_intcomma(value):
    try:
        return "{:,}".format(value).replace(",", " ")
    except (ValueError, TypeError):
        return value
