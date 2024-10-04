from django.shortcuts import render
from rest_framework import viewsets

from .models import UserPereval, Status, Pereval, Coordinates
from .serializers import UserSerializaer, StatusSerializers, PerevalSerializers, CoordinatesSerializers


class UserApiView(viewsets.ModelViewSet):
    queryset = UserPereval.objects.all()
    serializer_class = UserSerializaer

class StatusApiView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers

class PerevalApiView(viewsets.ModelViewSet):
    queryset = Pereval
    serializer_class = PerevalSerializers

class Coordinates(viewsets.ModelViewSet):
    queryset = Coordinates
    serializer_class = CoordinatesSerializers
