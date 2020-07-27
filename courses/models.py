from django.db import models
from datetime import datetime

GENDER = (
    ('female','FEMALE'),
    ('male','MALE'),
)

CHOOSE = (
    ('yes','YES'),
    ('no','NO'),
)

class Register(models.Model):
    fullname = models.CharField(max_length=200)
    birthdate = models.DateField()
    gender = models.CharField(max_length=7,choices=GENDER)
    pincode = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    gname = models.CharField(max_length=100)
    gphone = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=30)
    ques = models.CharField(max_length=3,choices=CHOOSE)
    def __str__(self):
        return self.fullname

class Enroll(models.Model):
    fullname = models.CharField(max_length=200)
    birthdate = models.DateField()
    gender = models.CharField(max_length=7,choices=GENDER)
    pincode = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    gname = models.CharField(max_length=100)
    gphone = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=30)
    ques = models.CharField(max_length=3,choices=CHOOSE)
    def __str__(self):
        return self.fullname