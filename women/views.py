from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from women.models import Women, Category
from women.serializers import WomenSerializer


class WomeViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()  # данные которые возвращаются ао запросу
    serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)  # @action Если у вас есть специальные методы, которые должны быть маршрутизируемыми, вы можете пометить их как таковые с помощью @action декоратора.
                                            # Как и обычные действия, дополнительные действия могут быть предназначены либо для одного объекта, либо для целой коллекции.
                                            # Чтобы указать это, задайте для detail аргумента значение True или False. Маршрутизатор соответствующим образом настроит свои шаблоны URL.
                                            # Например, DefaultRouter настроит подробные действия так, чтобы они содержали pk в своих шаблонах URL.
    def category(self, reauest, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': [c.name for c in cats.name]})


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


