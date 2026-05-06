from django.contrib import admin
from django.utils.html import format_html
from django.contrib import messages

from .models import Inventory, Tags

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'description', 'quantity', 'price', 'image']
    filter_horizontal = ('tags',)

    list_display = ('name', 'slug', 'description', 'quantity', 'price','stock_status', 'image_preview')
    actions = ['notify_low_stock']
    low_stock_threshold = 5

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />', obj.image.url)
        return "Нет фото"
    image_preview.short_description = 'Превью'

    def stock_status(self, obj):
        if obj.quantity <= 0:
            return "НЕТ В НАЛИЧИИ"
        elif obj.quantity <= self.low_stock_threshold:
            return f"Заканчивается (осталось {obj.quantity})"
        return "В наличии"
    stock_status.short_description = "Состояние остатка"

    def notify_low_stock(self, request, queryset):
        low_stock_items = queryset.filter(quantity__lte=self.low_stock_threshold)
        if not low_stock_items:
            self.message_user(request, "Среди выбранных товаров нет заканчивающихся.", level=messages.INFO)
            return
        report = "\n".join([f"{item.name} — остаток: {item.quantity}" for item in low_stock_items])
        self.message_user(request, f"Уведомление о заканчивающихся товарах:\n{report}", level=messages.WARNING)
    notify_low_stock.short_description = "Отправить уведомление о заканчивающихся товарах"