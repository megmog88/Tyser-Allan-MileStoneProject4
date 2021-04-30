from django.test import SimpleTestCase


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_merchandise_status_code(self):
        response = self.client.get('/merchandise/')
        self.assertEqual(response.status_code, 200)

    def test_home_contact_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
