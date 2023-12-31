from django.db import models

# Create your models here.
class skill(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class education(models.Model):
    duration = models.CharField(max_length=15)
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class achivement(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name

