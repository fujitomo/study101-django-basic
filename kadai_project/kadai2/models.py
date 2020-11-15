from django.db import models
from datetime import datetime
from django.contrib import admin


class KimetsuCharactorModel(models.Model):
    """鬼滅の刃キャラクターModel"""
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1)
    characteristic = models.CharField(max_length=300)
    create_dt = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class SexModel(models.Model):
    """性別マスタModel"""
    sex_id = models.CharField(max_length=2)
    value = models.CharField(max_length=10)
    create_dt = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.value
