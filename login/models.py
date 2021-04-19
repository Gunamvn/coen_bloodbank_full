from django.db import models
from django.contrib.auth.models import User
# from phone_field import PhoneField

class bbank(models.Model):
    firstname = models.CharField(null=True, blank=True, max_length=100)
    lastname = models.CharField(null=True, blank=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_age = models.IntegerField(null=True, blank=True)
    bloodgrp = models.CharField(null=True, blank=True, max_length=4)
    email = models.EmailField(null=True, blank=True, max_length=100)
    # mobile = PhoneField(null=True, blank=False, unique=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user_address = models.TextField(null=True, blank=False, max_length=300)

    def __str__(self):
        return self.firstname


class donarreg(models.Model):
    firstname = models.CharField(null=True, blank=True, max_length=100)
    lastname = models.CharField(null=True, blank=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_age = models.IntegerField(null=True, blank=True)
    bloodgrp = models.CharField(null=True, blank=True, max_length=4)
    email = models.EmailField(null=True, blank=True, max_length=100)
    # mobile = PhoneField(null=True, blank=False, unique=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user_address = models.TextField(null=True, blank=False, max_length=300)

    def __str__(self):
        return self.firstname