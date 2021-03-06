from rest_framework import generics
from rest_framework.response import Response

from amh_api.models import Level, Team
from amh_api.serializers import LevelSerializer, TeamSerializer


class LevelList(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelDetail(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelTeams(LevelDetail):
    def get(self, request, *args, **kwargs):
        teams = Team.objects.filter(level=self.get_object())
        return Response(TeamSerializer(teams, many=True, context={'request': request}).data)
