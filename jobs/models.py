from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Job(models.Model):
    technologies = models.ForeignKey(Technology, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.BooleanField()
    published = models.DateTimeField()
    description = models.CharField(max_length=300)
    def __str__(self):
        return self.title+': '+self.description