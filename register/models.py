from django.db import models

class Human(models.Model):
    name = models.CharField(max_length=33)
    email = models.EmailField()
    objects = models.Manager

    def __str__(self):
        return self.name

# Create your models here.
