from rest_framework.serializers import ModelSerializer
from .models import Category, Recipe


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
