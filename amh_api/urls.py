from django.conf.urls import url
from amh_api.views import base, clubs, levels, referees, teams, venues, players, matches, seasons, competitions

urlpatterns = [

    #referees URLs
    url(r'^referees/$', referees.RefereeList.as_view(), name='referee-list'),
    url(r'^referees/(?P<pk>[0-9]+)/$', referees.RefereeDetail.as_view(), name='referee-detail'),

    # venues URLs
    url(r'^venues/$', venues.VenueList.as_view(), name='venue-list'),
    url(r'^venues/(?P<pk>[0-9]+)/$', venues.VenueDetail.as_view(), name='venue-detail'),
    url(r'^venues/(?P<pk>[0-9]+)/matches$', venues.VenueMatches.as_view(), name='venue-matches'),

    # levels URLs
    url(r'^levels/$', levels.LevelList.as_view(), name='level-list'),
    url(r'^levels/(?P<pk>[0-9]+)/$', levels.LevelDetail.as_view(), name='level-detail'),
    url(r'^levels/(?P<pk>[0-9]+)/teams$', levels.LevelTeams.as_view(), name='level-teams'),

    # clubs URLs
    url(r'^clubs/$', clubs.ClubList.as_view(), name='club-list'),
    url(r'^clubs/(?P<pk>[0-9]+)/$', clubs.ClubDetail.as_view(), name='club-detail'),
    url(r'^clubs/(?P<pk>[0-9]+)/teams$', clubs.ClubTeams.as_view(), name='club-teams'),
    url(r'^clubs/(?P<pk>[0-9]+)/players$', clubs.ClubPlayers.as_view(), name='club-players'),

    # teams URLs
    url(r'^teams/$', teams.TeamList.as_view(), name='team-list'),
    url(r'^teams/(?P<pk>[0-9]+)/$', teams.TeamDetail.as_view(), name='team-detail'),
    url(r'^teams/(?P<pk>[0-9]+)/players$', teams.TeamPlayers.as_view(), name='team-players'),

    # player URLs
    url(r'^players/$', players.PlayerList.as_view(), name='player-list'),
    url(r'^players/(?P<pk>[0-9]+)/$', players.PlayerDetail.as_view(), name='player-detail'),

    # match URLs
    url(r'^matches/$', matches.MatchList.as_view(), name='player-list'),
    url(r'^matches/(?P<pk>[0-9]+)/$', matches.MatchDetail.as_view(), name='match-detail'),

    # season URLs
    url(r'^seasons/$', seasons.SeasonList.as_view(), name='season-list'),
    url(r'^seasons/(?P<pk>[0-9]+)/$', seasons.SeasonDetail.as_view(), name='season-detail'),
    url(r'^seasons/(?P<pk>[0-9]+)/competitions$', seasons.SeasonCompetitions.as_view(), name='season-competitions'),

    # competition URLs
    url(r'^competitions/$', competitions.CompetitionList.as_view(), name='competition-list'),
    url(r'^competitions/(?P<pk>[0-9]+)/$', competitions.CompetitionDetail.as_view(), name='competition-detail'),
    url(r'^competitions/(?P<pk>[0-9]+)/matches$', competitions.CompetitionMatches.as_view(), name='competition-matches'),
    url(r'^competitions/(?P<pk>[0-9]+)/teams', competitions.CompetitionTeams.as_view(), name='competition-teams'),
    url(r'^competitions/(?P<pk>[0-9]+)/statistics', competitions.CompetitionStatistics.as_view(), name='competition-statistics'),


    url(r'^$', base.api_root)
]
