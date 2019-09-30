# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from datetime import datetime, date
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[a-zA-Z]+$')

class pursemanager(models.Manager):
    def validator(self, postData):
        errors ={}
        if len(postData['name']) < 2:
            errors['name1']="Name should be more than 2 characters"
        if len(PurseName.objects.filter(pursename=postData['pursename'])) > 0:
            errors['pursename']="The purse' name already exists"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email2']="Your email is invalid."
        return errors
# Create your models here.
class PurseName(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Purse(models.Model):
    pursename = models.ForeignKey(PurseName, related_name="pursename")
    image=models.ImageField(upload_to = 'img/', default = 'img/no-img.jpg')
    description=models.TextField(max_length=1000)
    dimmensions=models.CharField(max_length=255)
    extrainfo=models.CharField(max_length=255, default="")
    weight=models.CharField(max_length=255)
    color=models.CharField(max_length=7,default="#000000")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = pursemanager()