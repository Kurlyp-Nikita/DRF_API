from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # для того пользователя кто создал запись, HiddenField - скрытое поле пользователя

    class Meta:
        model = Women
        fields = '__all__'
