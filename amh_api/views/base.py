from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'referees': reverse('referee-list', request=request, format=format),
        'venues': reverse('venue-list', request=request, format=format),
        'clubs': reverse('club-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'players': reverse('player-list', request=request, format=format),
        'levels': reverse('level-list', request=request, format=format),
        'seasons': reverse('season-list', request=request, format=format),
        'competitions': reverse('competition-list', request=request, format=format),
    })
