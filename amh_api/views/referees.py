from rest_framework import generics
from rest_framework.response import Response
from django.db import models

from amh_api.models import Referee, Match
from amh_api.serializers import RefereeSerializer, MatchSerializer, SimpleMatchSerializer


class RefereeList(generics.ListCreateAPIView):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer


class RefereeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer


class RefereeMatches(RefereeDetail):
    def get(self, request, *args, **kwargs):
        condition = models.Q(referee_a=self.get_object()) | models.Q(referee_b=self.get_object()) | \
                    models.Q(timekeeper=self.get_object()) | models.Q(scorer=self.get_object())
        competitions = Match.objects.filter(condition).order_by('-stage')
        return Response(SimpleMatchSerializer(competitions, many=True, context={'request': request}).data)