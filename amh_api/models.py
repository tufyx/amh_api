from __future__ import unicode_literals

from django.db import models
from amh_api.enums import Gender, Status, Points
from datetime import date
from collections import deque
from random import shuffle, randint


class Level(models.Model):
    GENDER_CHOICES = [(Gender.MALE, 'male'),
                      (Gender.FEMALE, 'female')]
    name = models.CharField(max_length=255, blank=False)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=Gender.MALE)

    @property
    def description(self):
        return '{name} {gender}'.format(name=self.name, gender=self.get_gender_display())


class Club(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image = models.CharField(max_length=255, blank=True, default='')

    @property
    def image_path(self):
        return 'http://127.0.0.1:8000/static/images/{img}'.format(img=self.image)

    def build_teams(self):
        levels = Level.objects.all()
        count_teams = randint(1, 3)
        index = 0
        selected = []
        while index < count_teams:
            level = levels[randint(0, levels.count() - 1)]
            while level in selected:
                level = levels[randint(0, levels.count() - 1)]
            selected.append(level)
            team_name = '{club_name} {level_name}'.format(club_name=self.name, level_name=level.description)
            t = Team(name=team_name, club=self)
            t.save()
            t.level.add(level)
            index += 1


class Referee(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    image = models.CharField(max_length=255, blank=True, default='')
    date_of_birth = models.DateField()


class Player(models.Model):
    GENDER_CHOICES = [(Gender.MALE, 'male'),
                      (Gender.FEMALE, 'female')]
    first_name = models.CharField(max_length=255, blank=False, default='A')
    last_name = models.CharField(max_length=255, blank=False, default='B')
    image = models.CharField(max_length=255, blank=True, default='')
    date_of_birth = models.DateField(default=date(1976, 1, 1))
    gender = models.IntegerField(choices=GENDER_CHOICES, default=Gender.MALE)
    club = models.ForeignKey(Club)


class Team(models.Model):
    name = models.CharField(max_length=255, blank=False)
    club = models.ForeignKey(Club)
    players = models.ManyToManyField(Player, related_name='players')
    level = models.ManyToManyField(Level, related_name='levels')


class Venue(models.Model):
    name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=True, default='')


class Season(models.Model):
    STATUS_CHOICES = [(Status.SCHEDULED, 'scheduled'),
                      (Status.IN_PROGRESS, 'in_progress'),
                      (Status.COMPLETED, 'completed')]
    name = models.CharField(max_length=255, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    last_stage = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=Status.SCHEDULED)


class Competition(models.Model):
    STATUS_CHOICES = [(Status.SCHEDULED, 'scheduled'),
                      (Status.IN_PROGRESS, 'in_progress'),
                      (Status.COMPLETED, 'completed')]
    name = models.CharField(max_length=255, blank=False)
    legs = models.IntegerField(default=1)
    status = models.IntegerField(choices=STATUS_CHOICES, default=Status.SCHEDULED)
    level = models.ForeignKey(Level)
    season = models.ForeignKey(Season)
    teams = models.ManyToManyField(Team, related_name='teams')

    def build_matches(self):
        from random import randint
        # make sure no garbage is in the DB for the current competition
        Match.objects.filter(competition=self).delete()

        competition_teams = list(self.teams.all())
        team_ids = [team for team in competition_teams]
        if len(team_ids) % 2 != 0:
            team_ids.append(None)

        matches = []

        stage = 1
        while stage < len(team_ids):
            half = len(team_ids) / 2
            first = team_ids[:1]
            rest = deque(team_ids[1:])
            rest.rotate()
            team_ids = first + list(rest)
            guest = team_ids[:half]
            host = team_ids[half:]
            host.reverse()
            matches.append([(g, h) for g,h in zip(guest,host) if g != None and h != None])
            stage += 1

        competition_matches = []
        venues = Venue.objects.all()
        for stage in matches:
            for match in stage:
                competition_matches.append(Match(home_team=match[0],
                                                 away_team=match[1],
                                                 competition=self,
                                                 venue=venues[randint(0, venues.count() - 1)]))
        Match.objects.bulk_create(competition_matches)

    def build_statistics(self):
        competition_teams = self.teams.all()
        for team in competition_teams:
            Statistics(competition=self, team=team).save()


    def build(self):
        # add the teams
        self.add_teams()
        # build the round robin tournament matches
        self.build_matches()
        # create dummy data for stats
        self.build_statistics()


    # TODO - remove the randomized element in this function
    def add_teams(self):
        teams = list(Team.objects.filter(level=self.level))
        shuffle(teams)
        selected_teams = teams[:randint(1, len(teams)/2)]
        for t in selected_teams:
            self.teams.add(t)

class Statistics(models.Model):
    competition = models.ForeignKey(Competition)
    team = models.ForeignKey(Team)
    wins = models.IntegerField(default=0, blank=True)
    draws = models.IntegerField(default=0, blank=True)
    lost = models.IntegerField(default=0, blank=True)
    goals_for = models.IntegerField(default=0, blank=True)
    goals_against = models.IntegerField(default=0, blank=True)
    points = models.IntegerField(default=0, blank=True)


class Match(models.Model):
    home_ht_score = models.IntegerField(default=0)
    away_ht_score = models.IntegerField(default=0)
    home_ft_score = models.IntegerField(default=0)
    away_ft_score = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, default='')
    stage = models.IntegerField(default=0)
    home_team = models.ForeignKey(Team, related_name='home_team')
    away_team = models.ForeignKey(Team, related_name='away_team')
    referee_a = models.ForeignKey(Referee, related_name='referee_a', blank=True, null=True)
    referee_b = models.ForeignKey(Referee, related_name='referee_b', blank=True, null=True)
    timekeeper = models.ForeignKey(Referee, related_name='timekeeper', blank=True, null=True)
    scorer = models.ForeignKey(Referee, related_name='scorer', blank=True, null=True)
    competition = models.ForeignKey(Competition)
    venue = models.ForeignKey(Venue, blank=True, null=True)

    def update(self, hht, hft, aht, aft, venue, ref_a, ref_b, timekeeper, scorer, stage):
        self.home_ht_score = hht
        self.home_ft_score = hft
        self.away_ht_score = aht
        self.away_ft_score = aft
        self.venue = venue
        self.referee_a = ref_a
        self.referee_b = ref_b
        self.timekeeper = timekeeper
        self.scorer = scorer
        self.stage = stage

        home_team_stat = Statistics.objects.get(team=self.home_team, competition=self.competition)
        away_team_stat = Statistics.objects.get(team=self.away_team, competition=self.competition)

        home_team_stat.goals_for += hft
        home_team_stat.goals_against += aft
        away_team_stat.goals_for += aft
        away_team_stat.goals_against += hft

        if hft > aft:
            home_team_stat.wins += 1
            away_team_stat.lost += 1

            home_team_stat.points += Points.WIN
        elif hft < aft:
            home_team_stat.lost += 1
            away_team_stat.wins += 1

            away_team_stat.points += Points.WIN
        else:
            home_team_stat.draws += 1
            away_team_stat.draws += 1

            home_team_stat.points += Points.DRAW
            away_team_stat.points += Points.DRAW

        home_team_stat.save()
        away_team_stat.save()
        self.save()
