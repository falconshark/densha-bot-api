from django.urls import path
from rest_framework import routers
from .views import RouteView

router = routers.SimpleRouter()
router.register(r'routes', RouteView, 'route-detail')
