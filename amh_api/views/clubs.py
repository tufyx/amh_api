from rest_framework import generics
from rest_framework.response import Response

from amh_api.models import Club, Team, Player
from amh_api.serializers import ClubSerializer, TeamSerializer, PlayerSerializer


class ClubList(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


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
