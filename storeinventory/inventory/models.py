from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator



def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ë': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 'c', 'т': 't', 'у': 'u', 'ф': 'f', 'x': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 's': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class Inventory(models.Model):
    class Status(models.IntegerChoices):
        NOT_AVAILABLE = 0, 'Нет в наличии'
        IN_STOCK = 1, 'В наличии'
    
    image = models.ImageField(blank=True, upload_to='images')

    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug',
                            validators=[
                                MinLengthValidator(5, message="Минимум 5 симовлов"),
                                MaxLengthValidator(100, message="Максимиум 100 симовлов")
                            ])
    is_available = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.IN_STOCK, verbose_name='В наличии')
    description = models.TextField(blank=True, verbose_name='Описание')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Время создания')  # в момент первого появления записи
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags', verbose_name='Теги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('inventory', kwargs={'inventory_slug': self.slug})



class Tags(models.Model):
    tag_name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Тег')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('tag_name',)

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})