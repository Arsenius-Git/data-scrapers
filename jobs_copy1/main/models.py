from django.db import models

# Create your models here.

class create_model(models.Model):
    job_name = models.CharField(max_length=30)
    min_experience = models.CharField(max_length=35)
    company_name = models.CharField(max_length=40)
    requirements = models.TextField(max_length=250)

    def __str__ (self):
        return f"{self.job_name} - {self.min_experience} \n {self.company_name} \n {self.requirements}"
class looking_for_offers(models.Model):
    job_name = models.CharField(max_length=50)
    experience = models.CharField(max_length=200)
    abilities = models.CharField(max_length=200)

    def __str__(self):
        return self.job_name