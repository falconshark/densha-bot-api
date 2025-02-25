from django.db import models

class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    created_at = models.CharField(max_length=256)

class Area(models.Model):
    area_name = models.CharField(max_length=256)
    area_id = models.CharField(max_length=256)

class Route(models.Model):
    route_name = models.CharField(max_length=256)
    route_type = models.CharField(max_length=256)
    route_id = models.CharField(max_length=256)