from django.db import models

# Create your models here.
# from travelproject.settings import STATIC_ROOT


class Demo(models.Model):
    # path = STATIC_ROOT
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics/')
    desc = models.TextField()
