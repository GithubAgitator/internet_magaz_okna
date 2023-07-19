from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.email, self.name)

    class Meta:
        verbose_name = "MySubcriber"
        verbose_name_plural = "A lot of Subscribers"

class Stati(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография")
    title = models.CharField(max_length=60)
    opisanie = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s %s" % (self.title, self.opisanie)

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статья"





