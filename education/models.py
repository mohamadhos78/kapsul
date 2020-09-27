from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=128,null=False,blank=False)
    created_at = models.DateField(auto_now=True)
    session = models.ForeignKey("Session",on_delete=models.CASCADE)
    description = models.CharField(max_length=512,null=False,blank=False)
    price = models.IntegerField(null=False,blank=False)
    members = models.IntegerField(null=False,blank=False)

class Session(models.Model):
    description = models.TextField()
    file = models.FileField(null=False,blank=False)