import time

from django.contrib.auth import authenticate
from django.template.backends import django
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import Client, TestCase
from pprint import pprint
# from django.apps import apps
# from django.contrib import auth
# from django.conf.global_settings import AUTH_USER_MODEL
from accounts.admin import validate_phone_number
from accounts.models import Tuser
from accounts.sendSms import send_verification_sms
from accounts.utils import generate_verification_code
from accounts.admin import UserCreationForm


class ActivationPageTest(TestCase):
    def test_register_can_save_a_user(self):
        c = Client()
        response = c.post('/register', {'username': 'testuser', 'phone_number': '0771234567','password1':'testuser','password2':'testuser'}, follow=False)
        pprint(response.content)
        # print response.status_code
        # print response.redirect_chain
        # pprint(response.context['form'])
        self.assertEqual(response.context['user'].username,'testuser')

    # def test_can_register_and_activate_user(self):
    #     c = Client()
    #     response = c.post('/register', {'username': 'testuser', 'phone_number': '0771234567','password1':'testuser','password2':'testuser'}, follow=True)
    #     self.assertEqual(response.context['user'].username,'testuser')
    #
    #     time.sleep(5)
    #     pprint(vars(response))
    #     print response.request['PATH_INFO']
    #     # print 1,Tuser.objects.get(username='testuser').is_active
    #     # print 2,authenticate(username='testuser',password='testuser')
    #     response2 = c.post(response.request['PATH_INFO'],{'verification_code':Tuser.objects.get(username='testuser').verification_code}, follow=True)
    #     # pprint(vars(response2))
    #     self.assertIn('Testuser', response2.content)

    # def test_generate_random_number(self):
    #     for i in range(1,101):
    #         v_code = generate_verification_code()
    #         print i,'-',v_code, len(v_code)==6
    #         # self.assertTrue(len(v_code)==6)

    # def test_register_wrong_number_fails(self):
    #     c = Client()
    #     response = c.post('/register', {'username': 'testuser', 'phone_number': '077223457','password1':'testuser','password2':'testuser')))
    #     # pprint(dir(response))
    #     self.assertIn('Please provide a valid MTN or Airtel number',response.content)
    #
    # def test_validate_phone_number(self):
    #     phones = [
    #         '1234567890',#Fake number
    #         '0741234567',#Smart 074
    #         '0731234567',#K2 073
    #         '0711234567',#utl 071
    #         '0791234567',#orange 079
    #         '0721234567',#vodafone 072
    #         '0771234567',#MTN 077
    #         '0781234567',#MTN 078
    #         '0751234567',#Airtel 075
    #         '0701234567',#Airtel 070
    #         '256771234567',#MTN 25677
    #         '256781234567',#MTN 25678
    #         '256751234567',#Airtel 25675
    #         '256701234567',#Airtel 25670
    #         '+256771234567',#MTN +25677
    #         '+256781234567',#MTN +25678
    #         '+256751234567',#Airtel +25675
    #         '+256701234567',#Airtel +25670
    #         '077123457',#MTN 077: Valid number missing a digit
    #     ]
    #
    #     for phone in phones:
    #         result = validate_phone_number(phone)
    #         print phone, result
    #         # if result is None:
    #         #     print phone, False
    #         # else:
    #         #     print result.group(),result is not None
    #     # self.assertTrue(result is not None)
    #
    # def test_send_verification_sms(self):
    #     phone_number = '256706471650'
    #     code = '123456'
    #     response = send_verification_sms(phone_number,code)
    #     self.assertIn(phone_number,response)

    # def test_login_inactive_user_redirects_to_activation(self):
    #     c = Client()
    #     response = c.post('/register', {'username': 'testuser', 'phone_number': '0779222337','password1':'testuser','password2':'testuser'}, follow=True)
    #     self.assertEqual(response.context['user'].username,'testuser')
    #
    #     time.sleep(5)
    #     response2 = c.post('/login', {'username':'testuser', 'password':'testuser'}, follow=True)
    #     self.assertIn('activate',response2.content)

    # def test_change_number_before_activation(self):
    #     c = Client()
    #     response = c.post('/register', {'username': 'testuser', 'phone_number': '0771234567','password1':'testuser','password2':'testuser'}, follow=True)
    #     #check if the change number url exists
    #     self.assertIn('href="/change_number/testuser',response.content )
    #
    #     # #check if detects repeated number
    #     # response = c.post('/register', {'username': 'testuser1', 'phone_number': '0703426511','password1':'testuser1','password2':'testuser1'}, follow=True)
    #     # response2 = c.post('/change_number/testuser',{'phone_number':'0703426511'})
    #     # self.assertIn('This phone number is already registered with another user.',response2.content)
    #
    #     response3 = c.post('/change_number/testuser',{'phone_number':'0703426511'}, follow=True)
    #     self.assertIn('Activate account',response3.content)

    # def test_user_can_provide_referrer_username(self):
    #     c = Client()
    #     response = c.post('/register', {'username': 'testuser11', 'phone_number': '0771234567','password1':'testuser','password2':'testuser','referrer':'m'}, follow=True)
    #     self.assertIn('Please provide a valid username of leave the field blank',response.content)



# Create your tests here.
# user = apps.get_model(AUTH_USER_MODEL)
# user = auth.get_user_model()
# e = user.objects.all()[0]
# au = auth.authenticate(username=e.username,password="emmanuel")
#
# assert e == au,"Objects dont match"
# assert e.is_admin
# assert e.is_staff
# assert e.is_active