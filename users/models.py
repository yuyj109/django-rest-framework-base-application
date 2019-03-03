from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from model_utils.choices import Choices


class Profile(TimeStampedModel):
    GENDERS = Choices(
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=GENDERS.M)
    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username
