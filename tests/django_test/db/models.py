from django.contrib import admin
from django.urls import path
from django.db import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer


class SampleModel(models.Model):
    name = models.CharField("name", max_length=32)

class SampleModelSerializer(ModelSerializer):
    class Meta:
        model = SampleModel
        fields = "__all__"
