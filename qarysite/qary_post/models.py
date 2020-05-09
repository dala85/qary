from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={pk: self.pk})
