from django.test import SimpleTestCase

# Create your tests here


class SimpleTests(SimpleTestCase):

    def test_landscaping_page_status_code(self):
        response = self.client.get('/landscaping/')
        self.assertEqual(response.status_code, 200)

    def test_landscapinginfo_page_status_code(self):
        response = self.client.get('/landscapinginfo/')
        self.assertEqual(response.status_code, 200)
