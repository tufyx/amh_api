from rest_framework import generics
from rest_framework.response import Response

from amh_api.models import Team
from amh_api.serializers import TeamSerializer, PlayerSerializer, SimpleTeamSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamPlayers(TeamDetail):
    def get(self, request, *args, **kwargs):
        return Response(PlayerSerializer(self.get_object().players, many=True, context={'request': request}).data)
