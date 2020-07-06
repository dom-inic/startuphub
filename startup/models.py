from django.db import models

# Create your models here.

class Startup(models.Model):
    """ basic features for the startup"""
    name = models.CharField(max_length=50)
    funding = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='startup_pics')
    description = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Startups'

    def __str__(self):
        """ return a string representation of the model"""
        return self.name

    

class Descriptions(models.Model):
    """ more description about the startup"""
    name = models.ForeignKey(Startup, on_delete=models.CASCADE)
    text = models.TextField(max_length=800)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Descriptions'

    def __str__(self):
        return self.text[:50] + "...."
    

    