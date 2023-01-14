from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
User = get_user_model()
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        user = User.objects.get(email=username)
        print(user)
        return user