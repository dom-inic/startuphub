from django.db import models

# Create your models here.

class Startup(models.Model):
    """ basic features for the startup"""
    Choices = (
        ("science", "science"),
        ("Technology", "Technology"),
        ("Agriculture", "Agriculture"),
        ("Energy & Petroleum", "Energy & petroleum"),
        ("Industrial", "Industrial"),
        ("space", "Space"), 
        ("Health", "Health"),
        ("Tourism", "Tourism")
        )
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=Choices, default="Technology")
    funding = models.CharField(max_length=50)
    funding_reason = models.TextField()
    image = models.ImageField()
    description = models.TextField()
    location = models.CharField(max_length=50)
    address = models.CharField(max_length= 200, default="P.O BOX 4050 Nairobi")
    email = models.EmailField(default="startup@gmail.com")
    phone_no = models.IntegerField()
    website = models.URLField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Startups'

    def __str__(self):
        """ return a string representation of the model"""
        return self.name

    

# class Descriptions(models.Model):
#     """ more description about the startup"""
#     name = models.ForeignKey(Startup, on_delete=models.CASCADE)
#     text = models.TextField(max_length=800)
#     date_added = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = 'Descriptions'

#     def __str__(self):
#         return self.text[:50] + "...."
    

    