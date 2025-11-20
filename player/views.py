from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from places.models import Route
from places.models import Place

@api_view(['GET'])
def create_player(request):
    start_place = Place.objects.first()
    if not start_place:
        return Response(
            {"error": "Nincs egyetlen Place sem az adatbázisban. Hozz létre legalább egy helyet."},
            status=status.HTTP_400_BAD_REQUEST
        )

    player_count = Player.objects.count() + 1
    name = f"Player {player_count}"

    try:
        player = Player.objects.create(
            name=name,
            current_place=start_place
        )
    except Exception as e:
        return Response(
            {"error": f"A Player létrehozása nem sikerült: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return Response({
        "message": "Player sikeresen létrehozva",
        "player_id": player.id,
        "name": player.name,
        "code": player.code,
        "current_place": player.current_place.name,
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def move_player(request):
    player_code = request.data.get("player_code")
    destination_slug = request.data.get("destination_slug")

    if not player_code or not destination_slug:
        return Response({"error": "Hiányzó player_code vagy destination_slug"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        player = Player.objects.get(code=player_code)
    except Player.DoesNotExist:
        return Response({"error": "Nincs ilyen Player"}, status=status.HTTP_404_NOT_FOUND)

    try:
        destination = Place.objects.get(slug=destination_slug)
    except Place.DoesNotExist:
        return Response({"error": "Nincs ilyen Place"}, status=status.HTTP_404_NOT_FOUND)

    possible_routes = Route.objects.filter(from_place=player.current_place, to_place=destination)
    if not possible_routes.exists():
        return Response({"error": f"A Player nem tud ide menni: {player.current_place} -> {destination}"},
                        status=status.HTTP_400_BAD_REQUEST)
    player.current_place = destination
    player.save()

    return Response({
        "message": f"{player.name} áthelyezve {destination.name}-re",
        "player_id": player.id,
        "current_place": player.current_place.name,
    }, status=status.HTTP_200_OK)