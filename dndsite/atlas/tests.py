import datetime

from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

from .models import Detail


class LocationModelTests(TestCase):

    def test_str_with_short_text(self):
        """
        __str__() will return the whole string for details with less than 20
        characters in them.
        """
        detail_text = "string length of 19"
        detail = Detail(detail_text=detail_text)
        self.assertIs(detail.__str__(), detail_text)
