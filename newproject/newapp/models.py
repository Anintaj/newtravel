from django.db import models

# Create your models here.
class newdb(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

class team(models.Model):
    Name=models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos')
    about = models.TextField()




