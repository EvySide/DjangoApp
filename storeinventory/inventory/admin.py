from django.contrib import admin
from django.utils.html import format_html

from .models import Inventory, Tags

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'description', 'quantity', 'price', 'image']
    filter_horizontal = ('tags',)

    list_display = ('name', 'slug', 'description', 'quantity', 'price','image_preview')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />', obj.image.url)
        return "Нет фото"
    image_preview.short_description = 'Превью'

