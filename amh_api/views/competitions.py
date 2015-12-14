from rest_framework import generics
from rest_framework.response import Response

from amh_api.models import Competition, Match, Statistics
from amh_api.serializers import CompetitionSerializer, SimpleMatchSerializer, SimpleTeamSerializer, StatisticsSerializer


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionMatches(generics.RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def get(self, request, *args, **kwargs):
        matches = Match.objects.filter(competition=self.get_object())
        return Response(SimpleMatchSerializer(matches, many=True, context={'request': request}).data)


class CompetitionTeams(generics.RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def get(self, request, *args, **kwargs):
        return Response(SimpleTeamSerializer(self.get_object().teams, many=True, context={'request': request}).data)


class CompetitionStatistics(generics.RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def get(self, request, *args, **kwargs):
        statistics = Statistics.objects.filter(competition=self.get_object()).order_by('-points', '-goals_for')
        return Response(StatisticsSerializer(statistics, many=True, context={'request': request}).data)
