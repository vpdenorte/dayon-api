# from datetime import datetime, timezone
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializers
# from django.shortcuts import get_object_or_404


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = models.Visitor.objects.all()
    serializer_class = serializers.VisitorSerializer

    # def perform_create(self, serializer):
    #     serializer = self.serializer_class(data=self.request.data)
    #     if serializer.is_valid():
    #         card = serializer.validated_data.get('card')
    #         serializer.save(card=card)

    # def retrieve(self, request, pk='id'):
    #     visitor = models.Visitor.objects.get(pk=pk)

    #     if visitor.card != None:

    #         return Response({
    #             'first_name': visitor.first_name,
    #             'last_name': visitor.last_name,
    #             'destination': visitor.destination,
    #             'card': {
    #                 'uid': visitor.card.uid,
    #                 'alias': visitor.card.alias
    #             }
    #         })
    #     else:
    #         return Response({
    #             'first_name': visitor.first_name,
    #             'last_name': visitor.last_name,
    #             'destination': visitor.destination,
    #             'card': None
    #         })


class CardViewSet(viewsets.ModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer

    # def retrieve(self, request, pk='uid'):
    #     queryset = models.Card.objects.all()
    #     card = get_object_or_404(queryset, pk=pk)

    #     if card.visitor != None:
    #         visitor = models.Visitor.objects.get(card=pk)
    #         card.is_expired = visitor.expires_on < datetime.now(
    #             timezone.utc)
    #         print(card.visitor)

    #     serializer = serializers.CardSerializer(card)

    #     return Response(serializer.data)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = models.AccessLog.objects.all()
    serializer_class = serializers.AccessLogSerializer
