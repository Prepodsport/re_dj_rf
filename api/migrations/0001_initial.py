# Generated by Django 4.2.2 on 2023-06-20 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Салаты', 'Салаты'), ('Закуски', 'Закуски'), ('Первые блюда', 'Первые блюда'), ('Вторые блюда', 'Вторые блюда'), ('Десерты', 'Десерты')], default='Салаты', max_length=20, unique=True)),
                ('slug', models.SlugField(default='salads', max_length=20)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('ingredients', models.TextField(blank=True, null=True, verbose_name='Ингридиенты')),
                ('instructions', models.TextField(blank=True, null=True, verbose_name='Шаги приготовления')),
                ('slug', models.SlugField(max_length=250, verbose_name='Слаг')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('preview', models.ImageField(null=True, upload_to='', verbose_name='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]
