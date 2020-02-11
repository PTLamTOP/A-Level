from django import template
from datetime import date

register = template.Library()


@register.simple_tag
def today():
    return date.today()