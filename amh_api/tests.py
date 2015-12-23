from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class RefereesTestCase(APITestCase):

    fixtures = ['test_fixtures.json']

    def test_list_referees(self):
        url = reverse('referee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_referee(self):
        url = reverse('referee-detail', kwargs={'pk': 580})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'date_of_birth': '1979-01-06', 'first_name': u'Julie', 'last_name': u'Bonaventura', 'id': 580})

    def test_retrieve_referee_matches(self):
        url = reverse('referee-matches', kwargs={'pk': 583})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, [{'date': None, 'venue': u'Boris Trajkovski Arena',
                                         'm': 'Flensburg Handewitt U17 male - HC Metalurg U17 male 35-36',
                                         'competition': 166L, 'stage': 13L},
                                        {'date': None, 'venue': u'Westfalenhalle',
                                         'm': 'HC Metalurg U17 male - Ikast Bording U17 male 37-32',
                                         'competition': 166L, 'stage': 12L}])