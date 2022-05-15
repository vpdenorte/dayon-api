from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from . import models

class RoomResource(resources.ModelResource):

    class Meta:
        model = models.Room


class VisitorResource(resources.ModelResource):

    class Meta:
        model = models.Visitor


class CardResource(resources.ModelResource):

    class Meta:
        model = models.Card


class LogResource(resources.ModelResource):

    class Meta:
        model = models.AccessLog


class RoomAdmin(ImportExportModelAdmin):
    resource_class = RoomResource


class VisitorAdmin(ImportExportModelAdmin):
    resource_class = VisitorResource


class CardAdmin(ImportExportModelAdmin):
    resource_class = CardResource


class LogAdmin(ImportExportModelAdmin):
    resource_class = LogResource


admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Visitor, VisitorAdmin)
admin.site.register(models.Card, CardAdmin)
admin.site.register(models.AccessLog, LogAdmin)

