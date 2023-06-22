from PIL import Image
from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    SALADS = 'Салаты'
    APPETIZERS = 'Закуски'
    SOUPS = 'Первые блюда'
    MAIN_COURSE = 'Вторые блюда'
    DESSERT = 'Десерты'

    CATEGORIES = (
        (SALADS, 'Салаты'),
        (APPETIZERS, 'Закуски'),
        (SOUPS, 'Первые блюда'),
        (MAIN_COURSE, 'Вторые блюда'),
        (DESSERT, 'Десерты'),
    )
    name = models.CharField('Категория', max_length=20, choices=CATEGORIES, default='Салаты', unique=True)
    slug = models.SlugField('Слаг', max_length=20, default='salads')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    title = models.CharField('Название', max_length=128)
    ingredients = models.TextField('Ингридиенты', null=True, blank=True)
    instructions = models.TextField('Шаги приготовления', null=True, blank=True)
    slug = models.SlugField(max_length=250, verbose_name='Слаг')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    preview = models.ImageField(null=True, verbose_name='Фото')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.preview.path)
        if img.height > 300 or img.width > 200:
            output_size = (300, 200)
            img.thumbnail(output_size)
            img.save(self.preview.path)

    def get_preview(self):
        return self.preview.url

    def preview_tag(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.get_preview())

    preview_tag.short_description = 'Превью'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
