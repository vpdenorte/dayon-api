from datetime import datetime, timedelta, timezone

from django.db import models
from django.db.models.fields import related


class Room(models.Model):
    board_id = models.CharField(max_length=8, primary_key=True)
    mac_address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_accepting = models.BooleanField(default=False)
    capacity = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.name


class Card(models.Model):
    uid = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=255)
    whitelisted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    registered_on = models.DateTimeField(auto_now_add=True)
    expires_on = models.DateTimeField(null=True)
    card = models.OneToOneField(
        Card,
        on_delete=models.PROTECT,
        null=True
    )
    rooms = models.ManyToManyField(Room, related_name="visitors")
    current_room = models.ForeignKey(
        Room, on_delete=models.PROTECT, related_name="occupants", null=True)

    def __str__(self):
        return self.first_name + self.last_name


class AccessLog(models.Model):
    AccessType = models.TextChoices('AccessType', 'in out')

    timestamp = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey(
        Card, on_delete=models.SET_NULL, null=True, related_name="logs")
    visitor = models.ForeignKey(
        Visitor, on_delete=models.SET_NULL, null=True, related_name="logs")
    room = models.ForeignKey(
        Room, on_delete=models.SET_NULL, null=True, related_name="logs")
    type = models.CharField(choices=AccessType.choices, max_length=10)
