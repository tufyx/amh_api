from rest_framework import generics
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response

from amh_api.models import Club, Team, Player
from amh_api.serializers import ClubSerializer, TeamSerializer, PlayerSerializer


class ClubList(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def post(self, request, *args, **kwargs):
        name = request.data.get('name', '')
        image = request.data.get('image', 'tile.png')
        Club(name=name, image=image).save()
        return Response(status=status.HTTP_201_CREATED)


class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def put(self, request, *args, **kwargs):
        name = request.data.get('name', '')
        image = request.data.get('image', 'tile.png')
        club = self.get_object()
        club.name = name
        if image != 'tile.png':
            club.image = image
        club.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        print("delete resource")
        # delete club players
        # delete club teams
        # delete teams from competitions
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClubTeams(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def get(self, request, *args, **kwargs):
        club = self.get_object()
        teams = Team.objects.filter(club=club)
        serializer = TeamSerializer(teams, many=True, context={'request': request})
        return Response(serializer.data)


class ClubPlayers(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def get(self, request, *args, **kwargs):
        club = self.get_object()
        players = Player.objects.filter(club=club)
        serializer = PlayerSerializer(players, many=True, context={'request': request})
        return Response(serializer.data)
