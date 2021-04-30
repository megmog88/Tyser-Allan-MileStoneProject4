from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):


def test_draping_page_status_code(self):
        response = self.client.get('/draping/')
        self.assertEqual(response.status_code, 200)


def test_drapinginfo_page_status_code(self):
        response = self.client.get('/drapinginfo/')
        self.assertEqual(response.status_code, 200)
