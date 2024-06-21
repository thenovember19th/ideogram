from django.db import models

class Ideogram(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='generated_image')