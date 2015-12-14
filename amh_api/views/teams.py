from rest_framework import generics
from rest_framework.response import Response
from django.db import models

from amh_api.models import Team, Match
from amh_api.serializers import TeamSerializer, PlayerSerializer, SimpleMatchSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamPlayers(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        return Response(PlayerSerializer(self.get_object().players, many=True, context={'request': request}).data)


class TeamMatches(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        competition_id = request.GET.get('competition_id', -1)
        condition = models.Q(home_team=self.get_object()) | models.Q(away_team=self.get_object()) & models.Q(competition = competition_id)
        matches = Match.objects.filter(condition).order_by('-stage')
        return Response(SimpleMatchSerializer(matches, many=True, context={'request': request}).data)