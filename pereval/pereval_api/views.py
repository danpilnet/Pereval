from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import UserPereval, Status, Pereval, Coordinates
from .serializers import UserSerializaer, StatusSerializers, PerevalSerializers, CoordinatesSerializers


class UserApiView(viewsets.ModelViewSet):

    queryset = UserPereval.objects.all()
    serializer_class = UserSerializaer

class StatusApiView(viewsets.ModelViewSet):

    queryset = Status.objects.all()
    serializer_class = StatusSerializers

class PerevalApiView(viewsets.ModelViewSet):

    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializers
    filterset_fields = ('user__email',)

    def create(self, request, *args, **kwargs):

        serializer = PerevalSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data['id'],
            })
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad request',
                'id': None
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка подключения',
                'id': None
            })

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'New':
            serializer = PerevalSerializers(pereval,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'state': '1',
                    'message': 'Запись успешно сохранена'
                })
            else:
                return Response({
                    'state': '0',
                    'message': serializer.errors
                })
        else:
            return Response({
                'state': '0',
                'message': f'Отклонено! Причина: {pereval.get.status.display()}'
            })

class CoordinatesApiView(viewsets.ModelViewSet):
    queryset = Coordinates
    serializer_class = CoordinatesSerializers
