from django.contrib import admin

from .models import Recipe, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'slug', 'created_at', 'preview_tag')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')


admin.site.site_title = 'Админ панель Рецепты'
admin.site.site_header = 'Админ панель Рецепты'
