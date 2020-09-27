from django.db import models
from django.contrib.auth.models import User


def resume_validator(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    validaton_list = [".pdf",'.docx','.doc']
    if ext not in validaton_list:
        return ValidationError("Unsupported file format!")


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #course = models.ManyToManyField('Course')
    profile = models.ImageField(null=True,upload_to='files/student_profile')
    resume = models.FileField(null=True,upload_to='files/student_resume',validators=[resume_validator])
    last_course = models.CharField(max_length=128)
    created_at = models.DateField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)

