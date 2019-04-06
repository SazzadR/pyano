from django import template

register = template.Library()


@register.simple_tag
def blog_title(text=None):
    if text is None:
        return 'Django Blog'
    return 'Django Blog | {}'.format(text)
