from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class userManager(BaseUserManager):
    def create_user(self,email,password=None):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user



class customeUser(AbstractBaseUser):
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=100)

    objects = userManager()
    USERNAME_FIELD = 'email'

    
