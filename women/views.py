from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from women.models import Women
from women.serializers import WomenSerializer


# ListCreateAPIView. Используется для конечных точек чтения-записи для представления коллекции экземпляров модели.
# Предоставляет обработчики методов get и post.
# Расширяет: GenericAPIView, ListModelMixin, CreateModelMixin


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()  # данные которые возвращаются ао запросу
    serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset


# UpdateAPIView. Используется только для конечных точек обновления для одного экземпляра модели.
# Предоставляет обработчики методов put и patch.
# Расширяет: GenericAPIView, UpdateModelMixin


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()  # данные которые возвращаются ао запросу
    serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset


# RetrieveUpdateDestroyAPIView. Используется для конечных точек чтения, записи и удаления для представления одного экземпляра модели.
# Предоставляет обработчики методов get, put, patch и delete.
# Расширяет: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()  # данные которые возвращаются ао запросу
    serializer_class = WomenSerializer  # класс serializer_class, который обрабатывает queryset


# class WomenAPIView(APIView):
#     def get(self, request):
#         lst = Women.objects.all()
#         return Response({'posts': WomenSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects dose not axists"})
#
#         serialisers = WomenSerializer(data=request.data, instance=instance)
#         serialisers.is_valid(raise_exception=True)
#         serialisers.save()
#         return Response({'post': serialisers.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Objects dose not axists"})
#         return Response({"post": "delete post " + str(pk)})




# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

