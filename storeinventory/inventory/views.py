from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from jedi.inference.flow_analysis import Status

from inventory.models import Inventory, Tags

menu = [
    {'title': "О сайте", 'url_name': 'about'}
]


def index(request):
    inventory_units = Inventory.objects.prefetch_related('tags').all()

    data = {
        'title': 'Наши товары',
        'menu': menu,
        'inventory_units': inventory_units,
        'page_name': 'index',
        'tag_selected': None,
    }
    return render(request, "inventory/index.html", context=data)



def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
        'page_name': 'about',
        'tag_selected': None,
    }
    return render(request, "inventory/about.html", context=data)



def show_inventory(request, inventory_slug):
    inventory_unit = get_object_or_404(Inventory.objects.prefetch_related('tags'),
                                       slug=inventory_slug)

    data = {
        'title': inventory_unit.name,
        'menu': menu,
        'inventory_unit': inventory_unit,
        'page_name': 'index',
        'tag_selected': None,
    }

    return render(request, "inventory/inventory_unit.html", context=data)



def show_tag_list(request, tag_slug):
    tag = get_object_or_404(Tags, slug=tag_slug)
    inventory_units = tag.tags.all()

    data = {
        'title': f"Тег: {tag.tag_name}",
        'menu': menu,
        'inventory_units': inventory_units,
        'page_name': 'index',
        'tag_selected': tag.slug,
    }

    return render(request, 'inventory/index.html', context=data)



def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")


