# -*- coding: utf-8 -*-

from models import Club, Level, Referee, Venue, Team, Player, Season, Competition, Match, Statistics
from enums import Gender
from datetime import date
from random import randint, shuffle
from django.db import models

clubs = ['THW Kiel', 'MKB Veszprem', 'Paris St-Germain', 'Flensburg Handewitt', 'KIF Kolding', 'Montpelier AHB',
         'FC Barcelona', 'Ciudad Real', 'CAI Aragon', 'SC Benfica', 'ABC Braga', 'Rhein Neckar Lowen', 'Hamburg SV',
         'Minaur Baia Mare', 'Kadetten Schafhausen', 'HC Metalurg', 'Vardar Skopje', 'Vive Kielce', 'Orlen Wisla Plock',
         'Pick Szeged', 'HBC Nantes', 'IFK Hammarby', 'Motor Zaporoje', 'Skjern Handball', 'RK Zagreb',
         'Elverum Handball', 'Tatran Presov', 'Besiktas Istanbul', 'Rostov-Don', 'Larvik H.K.', 'RK Krim Ljubljana',
         'FTC Rail Cargo', 'Thuringer HC', 'Fleury-Loiret', 'Podravka Vegeta', 'Gyori ETO', 'Ikast Bording',
         'Viborg H.K.', 'Buducnost Podgorica', 'CSM Bucuresti', 'IK Savehof', 'MKS Selgros Lublin']

referees = ['Charlotte Bonaventura', 'Julie Bonaventura', 'Diana-Carmen Florescu', 'Anamaria Duţă',
            'Carlos María Mariana','Darío Leonel Minore', 'Yalatima Coulibali', 'Mamoudou Diabaté', 'Matija Gubica',
            'Boris Milošević', 'Václav Horáček', 'Jiří Novotný', 'Per Olesen', 'Lars Ejby Pedersen', 'Oscar Raluy',
            'Ángel Sabroso', 'Nordine Lazaar', 'Laurent Reveret', 'Brian Bartlett', 'Allan Stokes', 'Lars Geipel',
            'Marcus Helbig', 'Gjorgi Nachevski', 'Slave Nikolov', 'Kenneth Abrahamsen', 'Arne M. Kristiansen',
            'Mansour Abdulla Al-Suwaidi', 'Saleh Jamaan Bamurtef', 'Nenad Krstič', 'Peter Ljubič', 'Nenad Nikolić',
            'Dušan Stojković']

levels = ['Senior', 'U21', 'U19', 'U17', 'U15']

venues = [('LanxessArena', 'Koln'), ('SAP Arena', 'Mannheim'), ('Color Line Arena', 'Hamburg'), ('Westfalenhalle', 'Dortmund'),
          ('SparkassenArena', 'Kiel'), ('Bordelandhalle', 'Magdeburg'), ('Copperbox', 'London'), ('Palau Blaugrana', 'Barcelona'),
          ('Laszlo Papp Arena', 'Budapest'), ('Boxen Arena', 'Herning'), ('Boris Trajkovski Arena', 'Skopje'),
          ('Ice Palace', 'St. Petersburg'), ('Sala Traian', 'Rm. Valcea'), ('Gyor Arena', 'Gyor'), ('Globen Arena', 'Stockholm'),
          ('Tauron Arena', 'Krakow'), ('Ergo Arena', 'Gdansk')]

men_first_names = ["Nikola", "Luka", "Jerome", "Daniel", "Samuel", "Thierry", "Mikael", "Cedric", "Luc", "Xavier", "William", "Gregory", "Benoit",
               "Mikkel", "Niklas", "Anders", "Rene", "Hans", "Bo", "Joakim", "Kasper", "Thomas", "Rasmus",
               "Stephen", "Jacob", "Maik", "Mikael", "Holger", "Lukas", "Uwe", "Patrick", "Max", "Torsten", "Rune", "Christian"
                "Tiago", "Raul", "Alberto", "Juan", "Mattias",
                "Gonzalo", "Kiril", "Filip", "Ivano", "Igor", "Matej", "Domagoj", "Marko"]

men_last_names = ["Karabatic", "Fernandez", "Narcisse", "Honrubia", "Omeyer", "Guigou", "Sorhaindo", "Abalo", "Barachet", "Accambray", "Dumoulin", "Kounkoud",
                  "Hansen", "Landin", "Eggert", "Toft-Hansen", "Lindberg", "Spellerberg", "Sondergaard", "Hvidt", "Mogensen", "Schmidt",
                  "Weinhold", "Machulla", "Jicha", "Krause", "Glandorf", "Gensheimer", "Groetzki", "Kaufmann", "Jansen", "Jensen", "Damke", "Moller",
                  "Gomes", "Entrerrios", "Garcia", "Lopez", "Guardiola", "Perez", "Lazarov",
                  "Vori", "Balic", "Buntic", "Kopljar", "Gaber", "Duvnjak", "Alilovic"]

women_first_names = ["Camilla", "Katrine", "Kristine", "Nora", "Heidi", "Linn", "Amanda", "Gro", "Karoline", "Anja", "Tea",
                     "Ludmila", "Irina", "Ekaterina", "Anna", "Marina", "Elena",
                     "Bernadette", "Yvette", "Anita", "Zsuzsanna", "Adrienn", "Gabriela", "Anniko", "Timea"
                     "Kinga", "Katarina", "Radmila", "Jovanka", "Biljana", "Ana", "Dragana", "Suzana"]

women_last_names = ["Herrem", "Lunde", "Mork", "Lokke", "Sulland", "Kurtovic", "Hammerseng", "Edin", "Riegelhuth",
                    "Postnova", "Bodnieva", "Bliznova", "Davidenko", "Sen", "Dmitrieva", "Sanko",
                    "Bodi", "Broch", "Gorbicz", "Tomori", "Orban", "Szucs", "Toth", "Kovacsics", "Byzdra", "Bulatovic", "Petrovic",
                    "Radicevic", "Pavicevic", "Radovic", "Jovanovic", "Cvijic", "Lazovic"]


def clean():
    Club.objects.all().delete()
    Level.objects.all().delete()
    Referee.objects.all().delete()
    Venue.objects.all().delete()
    Team.objects.all().delete()
    Player.objects.all().delete()
    Season.objects.all().delete()
    Competition.objects.all().delete()
    Match.objects.all().delete()
    Statistics.objects.all().delete()


def build_clubs():
    for c in clubs:
        club = Club(name=c)
        club.save()
        club.build_teams()


def build_levels():
    for l in levels:
        for g in Level.GENDER_CHOICES:
            level = Level(name=l, gender=g[0])
            level.save()


def build_venues():
    for v in venues:
        venue = Venue(name=v[0], address=v[1])
        venue.save()


def random_dob():
    year = randint(1970, 1985)
    month = randint(1, 12)
    day = randint(1, 28 if month == 2 else 30)
    return date(year, month, day)


def build_referees():
    for r in referees:
        name = r.rsplit(' ', 1)
        referee = Referee(first_name=name[0], last_name=name[1], date_of_birth=random_dob())
        referee.save()


def build_players():
    clubs = Club.objects.all()
    for c in clubs:
        # generate men
        men_count = randint(20, 30)
        index = 0
        while index < men_count:
            p = Player(first_name=men_first_names[randint(0, len(men_first_names) - 1)],
                       last_name=men_last_names[randint(0, len(men_last_names) - 1)],
                       date_of_birth=random_dob(),
                       gender=Gender.MALE,
                       club=c)
            p.save()
            index += 1

        # generate women
        women_count = randint(20, 30)
        index = 0
        while index < women_count:
            p = Player(first_name=women_first_names[randint(0, len(women_first_names) - 1)],
                       last_name=women_last_names[randint(0, len(women_last_names) - 1)],
                       date_of_birth=random_dob(),
                       gender=Gender.FEMALE,
                       club=c)
            p.save()
            index += 1


def build_seasons():
    count_seasons = 1 #randint(3, 6)
    index = 0
    year = 2011
    while index < count_seasons:
        start_date = date(year, 9, 15)
        end_date = date(year + 1, 5, 30)
        name = 'Season {start_date} - {end_date}'.format(start_date=start_date, end_date=end_date)
        Season(name=name, start_date=start_date, end_date=end_date).save()
        year += 1
        index += 1


def build_competitions():
    seasons = Season.objects.all()
    for s in seasons:
        count_competitions = 2 # randint(3,6)
        levels = Level.objects.all()
        index = 0
        while index < count_competitions:
            level = levels[randint(0, levels.count() - 1)]
            name = 'S_{id}-C_{index}'.format(id=s.id, index=index)
            c = Competition(name=name, level=level, season=s)
            c.save()
            c.build()
            index += 1


def update_matches():
    matches = Match.objects.all()
    referees = Referee.objects.all()
    venues = Venue.objects.all()

    ref_count = referees.count()
    venues_count = venues.count()
    fraction = 2 * matches.count() / 3
    for m in matches[:fraction]:
        hht = randint(10, 15)
        aht = randint(10, 15)
        hft = randint(20, 38)
        aft = randint(20, 38)
        venue = venues[randint(0, venues_count - 1)]
        referee_a = referees[randint(0, ref_count - 1)]
        referee_b = referees[randint(0, ref_count - 1)]
        timekeeper = referees[randint(0, ref_count - 1)]
        scorer = referees[randint(0, ref_count - 1)]
        stage = randint(1, 15)
        m.update(hht, hft, aht, aft, venue, referee_a, referee_b, timekeeper, scorer, stage)


# def build_team_players():
#     clubs = Club.objects.all()
#     for c in clubs[:1]:
#         teams_per_club = Team.objects.filter(club=c)
#         for team in teams_per_club:
#             print team.level
            # players_per_club = Player.objects.filter(condition = models.Q(club=c) | models.Q(gender=team.level.gender))
            # shuffle(players_per_club)
            # team.players.add(players_per_club[:14])

def bootstrap():
    clean()
    build_levels()
    build_venues()
    build_referees()
    build_clubs()
    build_players()
    # build_team_players()
    build_seasons()
    build_competitions()
    update_matches()