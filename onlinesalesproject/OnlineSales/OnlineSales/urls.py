"""OnlineSales URL Configuration

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
from ConsumerApp import urls

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show,name='main'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('addmrt/',views.addmrt,name='addmrt'),
    path('viewmrt/',views.viewmrt,name='viewmrt'),
    path('deletemrt/',views.deletemrt,name='deletemrt'),
    path('del/',views.delete,name='del'),
    path('savemrt/',views.savemrt,name='savemrt'),
    path('check_login/',views.Check_login.as_view()),
    path('saveproduct/',views.Saveproduct.as_view()),
    path('view_product/<int:mid>/',views.Viewproduct.as_view()),
    path('update/<int:pk>/',views.Update.as_view()),
    path('updateproduct/',views.Updateproduct.as_view()),
    path('delete/<int:p_no>/',views.Delete.as_view()),
    path('save_pwd/',views.Save_pwd.as_view()),
    path('ConsumerApp/',include('ConsumerApp.urls'))

]
