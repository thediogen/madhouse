from django import template

register = template.Library()

@register.filter(name="upper_case")
def upper_case(value):
    return value.upper()