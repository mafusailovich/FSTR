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
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]


CHOISES = {('1', 'new'), ('2', 'pending'),
           ('3', 'accepted'), ('4', 'rejected')}


class PerevalAdded(models.Model):
    date_added = models.DateTimeField(auto_now=True)
    beautytitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255,unique=True)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField()
    level_winter = models.CharField(max_length=255, blank=True)
    level_spring = models.CharField(max_length=255, blank=True)
    level_summer = models.CharField(max_length=255, blank=True)
    level_autumn = models.CharField(max_length=255, blank=True)
    status = models.CharField(choices=CHOISES, default='new', max_length=8)
    coord = models.OneToOneField('Coords', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Images(models.Model):
    title = models.CharField(max_length=255)
    img = models.BinaryField(editable=True, max_length=None)


class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    img = models.ForeignKey(Images, on_delete=models.CASCADE)


class PerevalAreas(models.Model):
    id_parent = models.BigIntegerField()
    title = models.TextField()

class IMGTEST(models.Model):
    img = models.ImageField(blank=True)
