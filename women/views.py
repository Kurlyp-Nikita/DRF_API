from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from women.models import Women
from women.serializers import WomenSerializer


class WomeViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()  # данные которые возвращаются ао запросу
    serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset


# # ListCreateAPIView. Используется для конечных точек чтения-записи для представления коллекции экземпляров модели.
# # Предоставляет обработчики методов get и post.
# # Расширяет: GenericAPIView, ListModelMixin, CreateModelMixin
#
#
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()  # данные которые возвращаются ао запросу
#     serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset
#
#
# # UpdateAPIView. Используется только для конечных точек обновления для одного экземпляра модели.
# # Предоставляет обработчики методов put и patch.
# # Расширяет: GenericAPIView, UpdateModelMixin
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()  # данные которые возвращаются ао запросу
#     serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset
#
#
# # RetrieveUpdateDestroyAPIView. Используется для конечных точек чтения, записи и удаления для представления одного экземпляра модели.
# # Предоставляет обработчики методов get, put, patch и delete.
# # Расширяет: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()  # данные которые возвращаются ао запросу
#     serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset


