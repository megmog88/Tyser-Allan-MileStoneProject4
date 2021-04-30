from django.test import SimpleTestCase

# Create your tests here


class SimpleTests(SimpleTestCase):

    def test_merchandise_page_status_code(self):
        response = self.client.get('/merchandise/')
        self.assertEqual(response.status_code, 200)

    def test_landscapinginfo_page_status_code(self):
        response = self.client.get('/merchandiseinfo/')
        self.assertEqual(response.status_code, 200)
