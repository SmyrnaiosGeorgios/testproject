from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CategoryStore(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"

class Store(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    description = models.TextField(max_length=300, blank=True)
    supported_games = models.ManyToManyField('Cardgame')
    ENTRY_CHOICES = [('Free','Free'), ('Paid','Paid')]
    entry_fee = models.TextField(max_length = 4, choices = ENTRY_CHOICES, default= 'Free')
    photo = models.CharField(max_length=30, blank=True)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return f"{self.name} : {self.city} : {self.address} : {self.description}"


class Cardgame(models.Model):
    title = models.CharField(max_length=20)
    publisher = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    releasedate = models.DateField()
    logo = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.title}"


class Referee(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=40)
    cardgames = models.ManyToManyField('Cardgame')
    age = models.IntegerField(null=True)
    description = models.TextField(max_length=100, blank=True)
    avatar = models.CharField(max_length=30, blank=True)
    SEX_CHOICES = [('Male','Male'), ('Female','Female')]
    gender = models.TextField(max_length = 6, choices = SEX_CHOICES, blank=True)
    likes = models.ManyToManyField(User, related_name= 'referee')


    def __str__(self):
        return f"{self.name} : {self.lastname} : {self.gender} : {self.description}"