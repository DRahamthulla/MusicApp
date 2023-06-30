from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager,User
from uuid import uuid4

from django.conf import settings
User = settings.AUTH_USER_MODEL
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    REQUIRED_FIELDS=['username']

    objects = UserManager()

    def __str__(self):
        return self.email
class MusicFile(models.Model):
    file = models.FileField(upload_to='music/')
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    image=models.ImageField(upload_to='music_files/',default='',null=True)
    file_path = models.CharField(max_length=255,default='',null=True)
    value=models.CharField(max_length=10,default='',null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.title