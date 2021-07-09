from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    lan_choice = (
        ("English", "English"),
        ("French", "French"),
        ("German", "German"),
        ("Hindi", "Hindi"),
        ("Chinese", "Chinese"),
        ("Spanish", "Spanish"),
        ("Russian", "Russian"),
        ("korean", "Korean"),
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=100, choices=lan_choice)
    info = models.TextField()

    dat_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
