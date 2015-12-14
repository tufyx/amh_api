from rest_framework import serializers
from amh_api.models import Referee, Level, Club, Venue, Team, Player, Season, Competition, Statistics


class RefereeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Referee
        fields = ('id', 'first_name', 'last_name', 'date_of_birth')


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name', 'gender')


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'address')


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name')


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    level = LevelSerializer()
    club = ClubSerializer()


class SimpleTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'club', 'gender')


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'name', 'start_date', 'end_date', 'last_stage', 'status')


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competition
        fields = ('id', 'name', 'status')


class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statistics
        fields = ('id', 'team', 'wins', 'draws', 'lost', 'goals_for', 'goals_against', 'points')
        depth=1


class MatchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    home_team = SimpleTeamSerializer()
    away_team = SimpleTeamSerializer()
    home_ft_score = serializers.IntegerField()
    away_ft_score = serializers.IntegerField()
    venue = VenueSerializer()
    date = serializers.DateTimeField()
    competition = CompetitionSerializer()


class SimpleMatchSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'm': '{home} - {away} {home_score}-{away_score}'.format(home=instance.home_team.name,
                                                                    away=instance.away_team.name,
                                                                    home_score=instance.home_ft_score,
                                                                    away_score=instance.away_ft_score),
            'venue': instance.venue.name,
            'date': instance.date,
            'stage': instance.stage,
            'competition': instance.competition.id
        }
