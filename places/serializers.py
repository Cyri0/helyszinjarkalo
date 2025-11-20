from rest_framework import serializers
from .models import Place, Route

class RouteSerializer(serializers.ModelSerializer):
    to_place_name = serializers.CharField(source='to_place.name', read_only=True)
    to_place_slug = serializers.CharField(source='to_place.slug', read_only=True)

    class Meta:
        model = Route
        fields = ['direction_name', 'to_place_name', 'to_place_slug']


class PlaceDetailSerializer(serializers.ModelSerializer):
    routes_from = RouteSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ['name', 'description', 'routes_from']
