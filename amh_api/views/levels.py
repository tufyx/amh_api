from rest_framework import generics
from rest_framework.response import Response

from amh_api.models import Level, Team
from amh_api.serializers import LevelSerializer, TeamSerializer


class LevelList(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelTeams(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    def get(self, request, *args, **kwargs):
        teams = Team.objects.filter(level=self.get_object())
        for t in teams:
            print t.level
        return Response(TeamSerializer(teams, many=True, context={'request': request}).data)
