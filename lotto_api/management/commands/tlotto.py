# from django.core.management.base import BaseCommand
# from daily_lotto.daily_l import *
# import schedule
# import time
# import africastalking
# from test_lotto import *
#
#
# class Command(BaseCommand):
#
#     help = 'Tossapp lotto'
#
#     def handle(self, *args, **options):
#         # Initialize SDK
#         username = "sandbox"
#         api_key = "40f73106539e336c14581a03dc5cac0badb322f68f7502dd65a3f1b93bf3db1c"
#         africastalking.initialize(username, api_key)
#
#         # Initialize a service e.g. SMS
#         sms = africastalking.SMS
#
#         # Use the service synchronously
#         response = sms.send("Hello Message!", ["+256705920191"])
#         print(response)
#
#
