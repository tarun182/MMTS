"""money URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from trans.views import trans

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.htm'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('DW/', include('DW.urls')),
    path('TransactionDetails/', trans),
    path('users/', include('django.contrib.auth.urls')),
    path('checkBal/',TemplateView.as_view(template_name='check_bal.htm'),name='check Bal'),
]
