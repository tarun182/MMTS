from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import deposit_view, withdraw_view

urlpatterns = [
    path('Deposit/', deposit_view, name='Deposit'),
    path('Withdraw/', withdraw_view, name='Withdraw'),
]