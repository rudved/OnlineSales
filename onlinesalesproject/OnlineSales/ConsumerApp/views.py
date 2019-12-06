from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, RedirectView

import ConsumerApp
from ConsumerApp.models import ConsumerModel
from app.models import ProductModel

class Loginc(TemplateView):
    template_name = 'Consumer/loginc.html'



class Registerc(CreateView):
    model = ConsumerModel
    template_name = 'Consumer/registerc.html'
    fields = '__all__'
    success_url = '/ConsumerApp/loginc/'



def savec(request):
    email = request.POST['email']
    password = request.POST['password']
    ConsumerModel.objects.get(email=email,password=password)
    return HttpResponse('OK')



def view_p(request):
    p = ProductModel.objects.all()
    return render(request,'Consumer/index1.html',{'data':p})


def p_details(request):
    p_no = request.GET['p_no']
    d = ProductModel.objects.get(p_no=p_no)
    return render(request,'Consumer/p_details.html',{'data':d})