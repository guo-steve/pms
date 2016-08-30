from django import template
import re

register = template.Library()

@register.filter(name='match')
def match(value, pattern):
    """Usage: {% if value|match:"regex" %}"""
    return re.match(pattern, value)

