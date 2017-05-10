from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.utils import timezone
from django.core.urlresolvers import reverse
from quiz.models import Question, Choice, Player, Personality, Compatibility


class ModelTest(TestCase):

    def create_whatever(self, title="INFJ", body="yes, this is only a test", body2="test too"):
        return Player.objects.create(player_text = body, personaltiy = title, facebook = body2, pub_date=timezone.now())

    def test_whatever_creation(self):
        w = self.create_Player()
        self.assertTrue(isinstance(w, Player))
        self.assertEqual(w.__unicode__(), w.title)

