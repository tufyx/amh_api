from rest_framework import generics

from amh_api.models import Match
from amh_api.serializers import MatchSerializer


class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetail(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

