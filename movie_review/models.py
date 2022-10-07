from email.policy import default
from random import choices
from re import A
from secrets import choice
from django.db import models
import os
from uuid import uuid4
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    # def date_upload_to(instance, filename):
    #     ymd_path = timezone.now().strftime('%Y/%m/%d')
    #     uuid_name = uuid4().hex
    #     extension = os.path.splitext(filename)[-1].lower()
    #     return '/'.join([
    #         ymd_path,
    #         uuid_name + extension,
    #     ])

    title = models.CharField(max_length=20)
    content = models.TextField()
    movie_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class nums(models.IntegerChoices):
        A = 5
        B = 4
        C = 3
        D = 2
        E = 1
    grade2 = models.IntegerField(choices=nums.choices, default=A)
    
    
    # photo = models.ImageField(upload_to='date_upload_to')