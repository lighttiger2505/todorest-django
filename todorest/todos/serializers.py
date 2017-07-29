# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('done', 'name', 'owner')
