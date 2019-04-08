import time
from pprint import pprint
from tossapp.models import *
from django.test import TestCase, Client


# Create your tests here.
from accounts.models import Tuser
from bs4 import BeautifulSoup as bs

"""
def get_this_profile(self, request, username):
    queryset = self.get_profile(username)
    if queryset:
        profile = UserProfileSerializer(queryset)
        game_played = Game_stat.objects.filter(user=queryset).count()
        referral_count = queryset.referrals.count()
        return Response(
            {'code': 1, 'response': profile.data, 'games_played': game_played, 'referral_count': referral_count})
    else:
        return Response({'message': "Does Not Exist", 'code': 0})
        """

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

class DashboardSettings(TestCase):
    def setUp(self):
        response = self.client.post('/register/', {'username': 'testuser', 'phone_number': '0771234567','password1':'testuser','password2':'testuser'}, follow=True)
        response2 = self.client.post(response.request['PATH_INFO'],{'verification_code':Tuser.objects.get(username='testuser').verification_code}, follow=True)

    def test_user_can_change_username(self):
        response = self.client.post("/dashboard/settings",{'form_name':'changeusernameform','current_username':'testuser','new_username':'testuser16','password':'testuser'}, follow=True)
        response2 = self.client.get('/logout?next=/',follow=True)
        response3 = self.client.post('/login', {'username':'testuser16', 'password':'testuser'}, follow=True)
        self.assertIn('Testuser16',response3.content)
        # print response.content

    def test_user_can_change_password(self):
        data = {'form_name':'changepasswordform','old_password':'testuser','new_password':'testuser16','retype_new_password':'testuser16'}
        response = self.client.post("/dashboard/settings",data, follow=True)
        response2 = self.client.get('/logout?next=/',follow=True)
        response3 = self.client.post('/login', {'username':'testuser', 'password':'testuser16'}, follow=True)
        self.assertIn('Testuser',response3.content)
        # print response