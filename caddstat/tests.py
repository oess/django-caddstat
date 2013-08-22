"""
CADD Stat tests
"""

from django.core import mail
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from .forms import FeedbackForm
import settings as caddstat_settings


class FeedbackTest(TestCase):
    """
    Send us some feedback
    """

    def setUp(self):
        self.client = Client()

    def test_feedback_form(self):
        """
        Test FeedbackForm only
        """

        correct_form_data = {
            'name': 'Joe Example',
            'email': 'joe@example.com',
            'message': 'feedback',
        }
        form = FeedbackForm(data=correct_form_data)
        self.assertTrue(form.is_valid())

        incorrect_form_data = {
            'name': 'Joe Example',
            'email': 'joeexample',
            'message': 'feedback',
        }
        form = FeedbackForm(data=incorrect_form_data)
        self.assertFalse(form.is_valid())

    def test_feedback_view(self):
        """
        Test the full view, including email
        """

        form_data = {
            'name': 'Joe Example',
            'email': 'joe@example.com',
            'message': 'feedback',
        }

        response = self.client.post(reverse('caddstat.views.feedback'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'caddstat/emails/feedback.txt')
        self.assertEqual(response.templates[1].name, 'caddstat/feedbackthanks.html')

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'CADD Stat feedback from {0}'.format(form_data['name']))
        self.assertEqual(mail.outbox[0].to, [caddstat_settings.CADDSTAT_FEEDBACK_EMAIL])
        self.assertEqual(mail.outbox[0].from_email, form_data['email'])