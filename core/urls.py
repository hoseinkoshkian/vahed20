
from django.contrib import admin
from django.urls import path , include
from .views import dashboardView
urlpatterns = [
    path('', dashboardView.as_view(), name='dashboard')


]
