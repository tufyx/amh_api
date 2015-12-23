from rest_framework import generics
from rest_framework.response import Response
from django.db import models

from amh_api.models import Team, Match, Competition, Level
from amh_api.serializers import TeamSerializer, PlayerSerializer, SimpleMatchSerializer, CompetitionSerializer, LevelSerializer


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


class TeamCompetitions(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        competitions = Competition.objects.filter(teams__id=self.get_object().id)
        return Response(CompetitionSerializer(competitions, many=True, context={'request': request}).data)


class TeamLevels(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        levels = self.get_object().level
        return Response(LevelSerializer(levels, many=True, context={'request': request}).data)