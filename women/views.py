from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from women.models import Women, Category
from women.serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from women.permiss import IsAdminOrReadOnly, IsOwnerOrReadOnly


# ListCreateAPIView. Используется для конечных точек чтения-записи для представления коллекции экземпляров модели.
# Предоставляет обработчики методов get и post.
# Расширяет: GenericAPIView, ListModelMixin, CreateModelMixin


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()  # данные которые возвращаются ао запросу
    serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset
    permission_classes = (IsAuthenticatedOrReadOnly, )


# UpdateAPIView. Используется только для конечных точек обновления для одного экземпляра модели.
# Предоставляет обработчики методов put и patch.
# Расширяет: GenericAPIView, UpdateModelMixin


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()  # данные которые возвращаются ао запросу
    serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )  # доступ только тем пользователям, которые получают доступ именно по токенам, по ссесиям нет.


# RetrieveUpdateDestroyAPIView. Используется для конечных точек чтения, записи и удаления для представления одного экземпляра модели.
# Предоставляет обработчики методов get, put, patch и delete.
# Расширяет: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class WomenAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()  # данные которые возвращаются ао запросу
    serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset
    permission_classes = (IsAdminOrReadOnly, )


