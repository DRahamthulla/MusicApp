from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from .models import MusicFile
from .views import music_search_view


class MusicSearchViewTestCase(TestCase):
    def setUp(self):
        # Create some test data
        self.music_file1 = MusicFile.objects.create(title='Song 1', artist='Artist 1')
        self.music_file2 = MusicFile.objects.create(title='Song 2', artist='Artist 2')
        self.music_file3 = MusicFile.objects.create(title='Another Song', artist='Artist 3')

    def test_music_search_view(self):
        # Prepare the request
        request = HttpRequest()
        request.method = 'GET'
        request.GET['query'] = 'song'

        # Call the view function
        response = music_search_view(request)

        # Check the response
        self.assertEqual(response.status_code, 200)  # Check for OK response
        self.assertTemplateUsed(response, 'search_results.html')  # Check the template used

        # Check the context data
        results = response.context['results']
        query = response.context['query']
        self.assertEqual(len(results), 2)  # Check the number of search results
        self.assertEqual(query, 'song')  # Check the query value

        # Check the search results
        self.assertIn(self.music_file1, results)
        self.assertIn(self.music_file2, results)
        self.assertNotIn(self.music_file3, results)

        # Perform more assertions as needed


# Note: Make sure to adjust the imports and model names based on your application structure.
