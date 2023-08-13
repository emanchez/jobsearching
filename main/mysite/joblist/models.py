from django.db import models

# Create your models here.


class JobListing(models.Model):
    jobUrl = models.CharField(max_length=2000)
    jobTitle = models.CharField(max_length=500)
    jobLocation = models.CharField(max_length=50)
    jobAttributes = models.CharField(max_length=500)
    jobDescription = models.CharField(max_length=500)

    def __unicode__(self):
        return self.jobTitle
