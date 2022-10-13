from atexit import register
from django import template
register = template.Library()

@register.filter
def my_upper(val):
    return val.upper() + ' RYU'