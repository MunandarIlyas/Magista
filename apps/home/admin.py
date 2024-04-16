# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from apps.home.models import Quiz, Kelas

# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ('nama', 'grup', 'skor')  # Specify which fields to display

admin.site.register(Quiz, QuizAdmin)    

admin.site.register(Kelas)