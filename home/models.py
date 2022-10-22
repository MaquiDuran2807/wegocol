from django.db import models

# Create your models here.
class ModelHome (models.Model):
    titulo = models.CharField (max_length= 150) 
    lema = models.CharField (max_length= 300)
    mision = models.CharField(max_length= 500) 
    vision = models.CharField (max_length= 500)