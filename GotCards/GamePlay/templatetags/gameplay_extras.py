from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter

@register.filter
def queryset_forloop(queryset, forloop_counter):
    return queryset[forloop_counter].value