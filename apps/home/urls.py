# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('get_user_data/<int:user_id>/', views.get_user_data_view, name='get_user_data'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('quiz_submission/', views.quiz_submission, name='quiz_submission'),
    path('eval_submission/', views.eval_submission, name='eval_submission'),
    path('kelas_list/', views.kelas_list, name='kelas-list'),
    path('quiz_list/', views.quiz_list, name='quiz_list'),
    path('eval_list/', views.eval_list, name='eval_list'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
