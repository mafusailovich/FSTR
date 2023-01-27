from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    otc = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)


    class Meta:
        constraints = [
            models.UniqueConstraint (fields=['email'], name='unique_email')
        ]


class PerevalAdded(models.Model):
    date_added = models.DateTimeField(auto_now=True)
    beautytitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField()
    level_winter = models.CharField(max_length=255)
    level_spring = models.CharField(max_length=255)
    level_summer = models.CharField(max_length=255)
    level_autumn = models.CharField(max_length=255)
    coord = models.OneToOneField('Coords', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)





class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Images(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(max_length=255)


class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    img = models.ForeignKey(Images, on_delete=models.CASCADE)

class PerevalAreas(models.Model):
    id_parent = models.BigIntegerField()
    title = models.TextField()
