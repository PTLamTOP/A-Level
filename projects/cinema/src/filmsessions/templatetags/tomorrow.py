from django import template
from datetime import date, timedelta

register = template.Library()


@register.simple_tag
def tomorrow():
    return date.today() + timedelta(days=1)