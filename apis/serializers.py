from rest_framework import serializers

from . import models


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = ('id', 'first_name', 'last_name', 'contact_number',
                  'registered_on', 'expires_on', 'card', 'rooms', 'current_room')
        # extra_kwargs = {
        #     'expires_on': {'required': False},
        #     'card': {'required': False},
        #     'current_room': {'required': False}
        # }


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = ('uid', 'name', 'whitelisted', 'visitor')
        # extra_kwargs = {
        #     'visitor': {'read_only': True}
        # }
        depth = 1


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ('board_id', 'mac_address', 'name', 'visitors',
                  'occupants', 'is_accepting', 'capacity', 'logs')
        depth = 1


class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccessLog
        fields = ('id', 'timestamp', 'card', 'visitor', 'room', 'type')
