from django.db.models import Q

from rest_framework import authentication
from rest_framework import exceptions
from accounts.models import Tuser


class TossApiAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        if not username:
            return None

        try:
            user = Tuser.objects.get(
                Q(username=username) | Q(phone_number=username)
            )
        except Tuser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return user, None


