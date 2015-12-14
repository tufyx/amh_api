from rest_framework import generics
from rest_framework.response import Response

from amh_api.models import Season, Competition
from amh_api.serializers import SeasonSerializer, CompetitionSerializer


class SeasonList(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonCompetitions(generics.RetrieveAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def get(self, request, *args, **kwargs):
        competitions = Competition.objects.filter(season=self.get_object())
        return Response(CompetitionSerializer(competitions, many=True, context={'request': request}).data)