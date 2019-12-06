"""MRTOnline URL Configuration

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
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mrtlogin),
    path('login/',views.login_check,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_product/',views.add_product,name='add_product'),
    path('save/',views.saveproduct,name='save'),
    path('view_product/',views.viewproduct,name='view_product'),
    path('update/',views.update,name='update'),
    path('update_p/',views.update_p,name='update_p'),
    path('delete/',views.delete,name='delete'),
    path('change_pwd/',views.change_pwd,name='change_pwd'),
    path('save_pwd/',views.save_pwd,name='save_pwd')
]
