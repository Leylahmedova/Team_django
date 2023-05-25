from django.db import models

class Player(models.Model):
    name=models.CharField(max_length=300)
    surname=models.CharField(max_length=300)
    age=models.FloatField()


    def __str__(self):
        return self.name
    
class Team(models.Model):
    name=models.CharField(max_length=300)
    rank=models.FloatField()
    players=models.ManyToManyField("product.Player",blank=True)
    def __str__(self):
        return self.name
    
