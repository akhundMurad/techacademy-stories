from atexit import register
from random import randint
from django import template


DEFAULT_IMAGE_SRC = "https://media.baamboozle.com/uploads/images/152185/1607591595_198751"


register = template.Library()


@register.filter(name="default_image")
def default_image(value: str) -> str:
    return value if value else DEFAULT_IMAGE_SRC


@register.simple_tag
def foods() -> int:
    return randint(100, 400)
