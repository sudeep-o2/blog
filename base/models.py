from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class Blog(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

