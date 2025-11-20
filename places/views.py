from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Place
from .serializers import PlaceDetailSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def place_detail(request, slug):
    place = get_object_or_404(Place.objects.prefetch_related('routes_from__to_place'), slug=slug)
    serializer = PlaceDetailSerializer(place)
    return Response(serializer.data, status=status.HTTP_200_OK)