from logging import raiseExceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Provider

from .serializers import CategorySerializer
from django.shortcuts import render


# Create your views here.
class CategoryListCreate(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self, request):
        category_serializer = CategorySerializer(data=request.data, many=False)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'Error al enviar datos al registrar categoría'}, status=status.HTTP_400_BAD_REQUEST)

class CategoryDeleteUpdate(APIView):
    def get(self, request, pk):
        category = Category.objects.all().filter(pk=pk).first()
        if category:
            serializer = CategorySerializer(category, many = True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'msg': 'Categoría no encontrada'}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        category = Category.objects.all().filter(pk=pk).first()
        if category:
            serializer = CategorySerializer(category, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({'msg': 'Categoría no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

