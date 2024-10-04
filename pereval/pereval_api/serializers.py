from rest_framework import serializers

from .models import UserPereval, Status, Pereval, Coordinates


class UserSerializaer(serializers.ModelSerializer):

    class Meta:
        model = UserPereval
        fields = ('full_name',
                  'last_name',
                  'pnone',
                  'email')

class StatusSerializers(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('user',
                  'status')

class PerevalSerializers(serializers.ModelSerializer):

    class Meta:
        model = Pereval
        fields = ('title',
                  'user',
                  'text')

class CoordinatesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Coordinates
        fields = ('longitude',
                  'latitude',
                  'height')
