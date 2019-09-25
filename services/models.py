from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/images')
    extra_field_heading = models.CharField(max_length=200, blank=True, null=True)
    extra_field_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

