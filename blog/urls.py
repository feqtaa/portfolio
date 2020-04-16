from django.contrib import admin
from django.urls import path
import jobs.views
from . import views

urlpatterns = [
                  path('', views.allblogs, name='blog/allblogs'),
                path('<int:blog_id>/', views.detail, name='detail')
              ]
