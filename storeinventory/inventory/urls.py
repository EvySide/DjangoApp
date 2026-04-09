from django.urls import path, register_converter
from django.views.defaults import page_not_found

from . import views
from . import converters

#добавляем ковертор для чисел архива
register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('inventory/<slug:inventory_slug>/', views.show_inventory, name='inventory'),
    path('tag/<slug:tag_slug>/', views.show_tag_list, name='tag'),
]

