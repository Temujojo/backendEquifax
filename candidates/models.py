from django.db import models

# Create your models here.

class CandidateJobs(models.Model):
    company= models.CharField(max_length=100)
    job= models.CharField(max_length=100)
    init_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.job

class CandidateEducation(models.Model):
    college= models.CharField(max_length=100)
    certificate= models.CharField(max_length=100)
    init_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.college
    
class Level(models.Model):
    level = models.CharField(max_length=50)
    def __str__(self):
        return self.level
    
class Language(models.Model):
    language = models.CharField(max_length=100)
    level= models.ForeignKey(Level, on_delete=models.CASCADE)
    def __str__(self):
        return self.language

class Candidate(models.Model):
    name= models.CharField(max_length=200)
    phone= models.CharField(max_length=20)
    email= models.CharField(max_length=80)
    description= models.CharField(max_length=300)
    job = models.ForeignKey(CandidateJobs, on_delete=models.CASCADE)
    education = models.ForeignKey(CandidateEducation, on_delete=models.CASCADE)
    language= models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


    