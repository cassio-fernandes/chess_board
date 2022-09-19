from rest_framework.routers import DefaultRouter

from pieces import viewsets

routers = DefaultRouter()

routers.register('pieces', viewset=viewsets.PieceViewSet)
