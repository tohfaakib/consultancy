from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slider_image = models.ImageField(upload_to='slider/images')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return "Slider Image"


class SliderText(models.Model):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
