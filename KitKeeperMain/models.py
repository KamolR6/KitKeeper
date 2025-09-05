from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=24)
    email = models.EmailField()

class League(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Shirt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=24)
    year_of_usage = models.IntegerField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.CharField(max_length=5, blank=True)
    condition = models.CharField(
        max_length=20,
        choices=[('new','New'),('used','Used')],
        default='used'
    )
    #image = models.ImageField(upload_to='shirts/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.team})"
