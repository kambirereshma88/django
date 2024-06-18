from django.db import models

# Create your models here.
class Movie(models.Model):
    #here we are not providing id,id will be given by django
    name = models.CharField(max_length=50)
    release_date= models.DateField()

    def __str__(self):
        return self.name