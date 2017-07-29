# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    done = models.BooleanField()
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User',
                              related_name='todos',
                              on_delete=models.CASCADE)
