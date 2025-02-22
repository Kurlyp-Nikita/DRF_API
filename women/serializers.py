import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Women


# class WomeModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'



# def encode():
#     model = WomeModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Angelina Jolie", "content": "Content: Angelina Jolie"}')
#     data = JSONRenderer().parse(stream)
#     serializers = WomenSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)
