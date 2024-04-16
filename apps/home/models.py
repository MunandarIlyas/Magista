# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    nama = models.CharField(max_length=100)
    grup = models.CharField(max_length=100)
    jawaban_soal_1 = models.CharField(max_length=7)
    jawaban_soal_2 = models.CharField(max_length=7)
    jawaban_soal_3 = models.CharField(max_length=7)
    jawaban_soal_4 = models.CharField(max_length=7)
    jawaban_soal_5 = models.CharField(max_length=7)
    skor = models.IntegerField()

    def __str__(self):
        return f"{self.nama} - {self.grup}"

class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=10)

    def __str__(self):
        return self.nama_kelas
