from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer


class RecipeView(ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def Routes(request):
    routes = [
        {
            'Точка': '/recipes/',
            'Метод': 'GET',
            'Описание': 'Возвращает массив рецептов'
        },
        {
            'Точка': '/categories/',
            'Метод': 'GET',
            'Описание': 'Возвращает массив категорий'
        },
        {
            'Точка': '/categories/id/',
            'Метод': 'GET',
            'Описание': 'Возвращает массив рецептов одной категории'
        },
        {
            'Точка': '/recipes/id/',
            'Метод': 'GET',
            'Описание': 'Возвращает один рецепт'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRecipes(request):
    categories = Recipe.objects.all()
    serializer = RecipeSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategory(request, pk):
    recipes = Recipe.objects.filter(category_id=pk)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRecipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)
