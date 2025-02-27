from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Route
from .serializers import RouteSerializer

    
class RouteView(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['=route_name']
    serializer_class = RouteSerializer
    queryset = Route.objects.all()