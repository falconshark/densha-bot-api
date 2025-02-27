from rest_framework import serializers
from .route_status import load_status
from .models import Route 
class RouteSerializer(serializers.ModelSerializer):
    route_status = serializers.SerializerMethodField()
    class Meta:
        model = Route 
        fields = ('id', 'route_name', 'route_url', 'route_status')
    def get_route_status(self, obj):
       return load_status(obj.route_url)    