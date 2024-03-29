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
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
