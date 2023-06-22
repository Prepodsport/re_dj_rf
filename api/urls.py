from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import CategoryView, RecipeView

from . import views

router = DefaultRouter()
router.register('categories', CategoryView)
router.register('recipes', RecipeView)

urlpatterns = [
    path('drf/', include(router.urls)),
    path('', views.Routes, name="routes"),
    path('recipes/', views.getRecipes, name="recipes"),
    path('categories/', views.getCategories, name="categories"),
    path('categories/<int:pk>/', views.getCategory, name="category"),
    path('recipes/<str:slug>/', views.getRecipe, name="recipe"),
    path('openapi', get_schema_view(
        title="RE_DJ_RF",
        description="Домашняя работа SkillFactory F4.6",
        version="1.0.0"
    ), name='openapi-schema'),
    path("swagger/", TemplateView.as_view(
        template_name="swagger-ui.html",
        extra_context={'schema_url': 'openapi-schema'}
    ), name="swagger-ui"),
]
