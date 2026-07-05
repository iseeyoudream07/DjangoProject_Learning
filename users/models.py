from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    phone = models.CharField('Phone Number', max_length=20, blank=True)
    location = models.CharField('Location', max_length=100, blank=True)
    bio = models.TextField('Personal introduction', blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

    def display_phone(self):
        return self.phone or '-'

    def display_location(self):
        return self.location or '-'
