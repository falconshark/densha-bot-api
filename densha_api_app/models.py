from django.db import models
class Route(models.Model):
    route_name = models.CharField(max_length=256)
    route_area = models.CharField(max_length=256)
    route_url = models.CharField(max_length=256)