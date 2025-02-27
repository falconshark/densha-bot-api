from django.shortcuts import render
from rest_framework import viewsets
from .models import Route
from .serializers import RouteSerializer

class RouteApiView(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

