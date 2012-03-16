'''
This module holds filters that can be used in postprocessing a form field.

@author: Gerson Galang
'''

from django import template
from django.utils.html import escape
from lxml.html.clean import Cleaner
from lxml.etree import ParserError


register = template.Library()


@register.filter
def size(value, actualSize):
    """Add the size attribute to the text field."""

    value.field.widget.attrs['size'] = actualSize
    return value


@register.filter
def parametername_form(value):
    "Removes all values of arg from the given string"
    return value.replace('/', '_s47_')

@register.filter
def sanitize_html(html, bad_tags=['body']):
   """Removes identified malicious HTML content from the given string."""
   try:
       if html is None or html == '':
          return html
       cleaner = Cleaner(style=False, page_structure=True, remove_tags=bad_tags,
             safe_attrs_only=False)
       return cleaner.clean_html(html)
   except ParserError:
       return escape(html)

       
