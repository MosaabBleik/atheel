from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self=None, request=None, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username.lower())
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None