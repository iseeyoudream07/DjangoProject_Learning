from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Topic(models.Model):
    txt = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.txt

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    txt = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.txt[:50]+("..." if len(self.txt) > 50 else "")

class Announcement(models.Model):
    content = models.TextField(verbose_name="Announcement")
    is_active = models.BooleanField(default=False,verbose_name="Display?")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:30]+("..." if len(self.content) > 30 else "")