# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib import messages

class UserManager(models.Manager):

    def validate(self,request, post_data):
        if len(post_data['full_name']) < 2 or len(post_data['alias']) < 2 or len(post_data['email']) < 2:
            messages.error(request, 'You need more than two letters')
        if request.POST['password'] != request.POST['confirmpw']:
            messages.error(request, 'your password must match')
        else:
            User.objects.create(
            full_name = request.POST['full_name'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = request.POST['password'],
            dob = request.POST['dob']
            )

    def validate_login(self, post_data):
        errors = []
        if len(self.filter(email=post_data['email'])) > 0:
            user = self.filter(email=post_data['email'])[0]
            errors.append('email incorrect again')
            #check user's password
        else:
            errors.append('email incorrect')

        if errors:
            return errors
        return user

class User(models.Model):
    full_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


    def __str__(self):
        return self.full_name + " " + self.email

class Friend(models.Model):
    friend_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    freinds = models.ForeignKey(User)
