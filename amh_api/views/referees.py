from rest_framework import generics

from amh_api.models import Referee
from amh_api.serializers import RefereeSerializer


class RefereeList(generics.ListCreateAPIView):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer


class RefereeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
