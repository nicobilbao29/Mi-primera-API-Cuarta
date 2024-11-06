from django.db import models

class CustomUser(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name