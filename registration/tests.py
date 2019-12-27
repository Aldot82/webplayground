from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('pacote', 'pacote@user.com', 'password1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='pacote').exists()
        self.assertEqual(exists, True)
