from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(upload_to='projects/images')

    def __str__(self):
        return self.title