from django.contrib import admin


from .models import Inventory, Tags

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'description', 'quantity', 'price']
    filter_horizontal = ('tags',)

    list_display = ('name', 'slug', 'description', 'quantity', 'price')


