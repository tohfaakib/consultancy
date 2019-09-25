from django.db import models

# Create your models here.

class About(models.Model):
    aboutImage = models.ImageField(upload_to='about/images')
    avoutVideo = models.URLField(null=True, blank=True)
    section_heading_one = models.CharField(max_length=200, null=True, blank=True)
    section_description_one = models.TextField(null=True, blank=True)
    section_heading_two = models.CharField(max_length=200, null=True, blank=True)
    section_description_two = models.TextField(null=True, blank=True)
    section_heading_three = models.CharField(max_length=200, null=True, blank=True)
    section_description_three = models.TextField(null=True, blank=True)
    section_heading_four = models.CharField(max_length=200, null=True, blank=True)
    section_description_four = models.TextField(null=True, blank=True)
    section_heading_five = models.CharField(max_length=200, null=True, blank=True)
    section_description_five = models.TextField(null=True, blank=True)
    section_heading_six = models.CharField(max_length=200, null=True, blank=True)
    section_description_six = models.TextField(null=True, blank=True)

    def __str__(self):
        return "About Us"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

