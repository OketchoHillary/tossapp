from accounts.models import Tuser
from django.db.models import Q


class TauthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False


    def get_user(self, user_id):
       try:
          return Tuser.objects.get(pk=user_id)
       except Tuser.DoesNotExist:
          return None

    def authenticate(self, username, password):
        try:
            user = Tuser.objects.get(
                Q(username=username) | Q(phone_number=username)
            )
        except Tuser.DoesNotExist:
            return None

        return user if user.check_password(password) else None