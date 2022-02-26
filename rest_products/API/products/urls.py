from django.urls import path

from .views import CategoryListCreate, CategoryDeleteUpdate

urlpatterns = [
    path('category/', CategoryListCreate.as_view()),
    path('category/<int:pk>/', CategoryDeleteUpdate.as_view()),    
]