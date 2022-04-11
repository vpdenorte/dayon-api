from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('visitor', views.VisitorViewSet)
router.register('card', views.CardViewSet)
router.register('room', views.RoomViewSet)
router.register('log', views.AccessLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
