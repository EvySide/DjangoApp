from django import template
from django.db.models import Count

from inventory.models import Tags


register = template.Library()

@register.inclusion_tag('inventory/list_tags.html', takes_context=True)
def show_all_tags(context):
    tags = Tags.objects.annotate(total=Count("tags")).filter(total__gt=0)
    return {
        'tags': tags,
        'tag_selected': context.get('tag_selected'),
    }

