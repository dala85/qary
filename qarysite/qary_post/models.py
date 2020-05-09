from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('qary_post:detail', kwargs={'pk': self.pk})
