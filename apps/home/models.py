# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kelas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama_kelas = models.CharField(max_length=10)

    def __str__(self):
        return self.nama_kelas

class Quiz(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    grup = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    jawaban_soal_1 = models.CharField(max_length=7)
    jawaban_soal_2 = models.CharField(max_length=7)
    jawaban_soal_3 = models.CharField(max_length=7)
    jawaban_soal_4 = models.CharField(max_length=7)
    jawaban_soal_5 = models.CharField(max_length=7)
    skor = models.IntegerField()

    def __str__(self):
        return f"{self.nama} - {self.grup}"
    
class Evaluasi(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    grup = models.ForeignKey('Kelas', on_delete=models.CASCADE)
    jawaban1 = models.CharField(max_length=100)
    skor1 = models.IntegerField()
    jawaban2 = models.CharField(max_length=100)
    skor2 = models.IntegerField()
    jawaban3 = models.CharField(max_length=100)
    skor3 = models.IntegerField()
    jawaban4 = models.CharField(max_length=100)
    skor4 = models.IntegerField()
    jawaban5 = models.CharField(max_length=100)
    skor5 = models.IntegerField()
    jawaban6 = models.CharField(max_length=100)
    skor6 = models.IntegerField()

    def __str__(self):
        return self.nama
    
class Eval(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    jawaban1 = models.TextField()
    skor1 = models.IntegerField(default=0)
    jawaban2 = models.TextField()
    skor2 = models.IntegerField(default=0)
    jawaban3 = models.TextField()
    skor3 = models.IntegerField(default=0)
    jawaban4 = models.TextField()
    skor4 = models.IntegerField(default=0)
    jawaban5 = models.TextField()
    skor5 = models.IntegerField(default=0)
    jawaban6 = models.TextField()
    skor6 = models.IntegerField(default=0)

    def __str__(self):
        return self.nama
