from rest_framework import generics
from rest_framework.response import Response

from amh_api.models import Venue, Match
from amh_api.serializers import VenueSerializer, MatchSerializer


class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class VenueMatches(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        matches = Match.objects.filter(venue=self.get_object())
        return Response(MatchSerializer(matches, many=True, context={'request': request}).data)