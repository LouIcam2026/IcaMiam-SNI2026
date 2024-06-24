from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='format_price')
@stringfilter
def format_price(value):
    try:
        value = float(value)

        return '{:.2f} €'.format(value)
    except:
        return value
    