import json
import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from app.models import MarchentModel,LoginModel,ProductModel
from .forms import Marchentform,ProductForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
# Create your views here.
def show(request):
    return render(request,'index.html')


def login(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')
    d = LoginModel.objects.filter(username=uname,password=pwd)
    if d :
       return render(request,'welcome.html')

def logout(request):
    return redirect('main')


def addmrt(request):
    return render(request,'addmrt.html')


def viewmrt(request):
    d = MarchentModel.objects.all()
    return render(request,"viewmrt.html",{"data":d})


def deletemrt(request):
    d = MarchentModel.objects.all()
    return render(request,'deletemrt.html',{"data":d})


def savemrt(request):
    idno = MarchentModel.objects.values_list('mrt_id')
    l = len(idno)
    if (l != 0):
        r = idno[l-1][0] + 1
    else:
        r = 1001
    name = request.POST.get('name')
    email = request.POST.get('email')
    cno = request.POST.get('cno')
    pw=random.randint(10000,99999)
    MarchentModel(mrt_id=r,mrt_name=name,Email_id=email,contactNo=cno,password=pw).save()
    return render(request,'welcome.html',{"message":"Marchent details are saved"})


def delete(request):
    idno = request.GET.get('idno')
    MarchentModel.objects.filter(mrt_id=idno).delete()
    return render(request,'deletemrt.html',{"message":'Record is deleted sucessfully'})


@method_decorator(csrf_exempt,name='dispatch')
class Check_login(View):
    def post(self,request,*args,**kwargs):
        data=request.body
        data2=json.loads(data)
        try:
            res=MarchentModel.objects.get(Email_id=data2['email'],password=data2['pwd'])
            json_data=serialize('json',[res])
            return HttpResponse(json_data,content_type='appilication/json')
        except:
            pass

@method_decorator(csrf_exempt,name='dispatch')
class Saveproduct(View):
    def post(self,request,*args,**kwargs):
        data = request.body
        data1 = json.loads(data)
        print(data1)
        try:
            ProductModel(p_no=data1['p_no'],p_name=data1['p_name'],p_price=data1['p_price'],
                         p_quantity=data1['p_qty'],m_id_id=data1['m_id_id']).save()
            return HttpResponse(status=200)
        except:
             pass


class Viewproduct(View):
    def get(self,request,mid):
        try:
            data=ProductModel.objects.filter(m_id_id=mid)
            json_data = serialize('json',data)
            return HttpResponse(json_data,status=200)
        except:
            return HttpResponse(status=400)


class Update(View):
    def get(self,request,pk):
        try:
            d = ProductModel.objects.get(p_no=pk)
            json_d = serialize('json',[d])
            print(json_d)
            return HttpResponse(json_d,status=200)
        except:
            return HttpResponse(status=400)

@method_decorator(csrf_exempt,name='dispatch')
class Updateproduct(View):
    def put(self,request,*args,**kwargs):
        new_data = json.loads(request.body)
        print(new_data)
        try:
            old_data = ProductModel.objects.get(p_no=new_data['p_no'])
            old_dic = {'p_id':old_data.p_no,'p_name':old_data.p_name,'p_price':old_data.p_price,
                        'p_quantity':old_data.p_quantity,'m_id':old_data.m_id_id}
        except:
             pass
        else:
            old_dic.update(new_data)
            ef = ProductForm(old_dic,instance=old_data)
            if ef.is_valid():
                ef.save()
                return HttpResponse(status=200)

@method_decorator(csrf_exempt,name='dispatch')
class Delete(View):
    def delete(self,request,p_no):
        ProductModel.objects.get(p_no=p_no).delete()
        return HttpResponse(status=200)

@method_decorator(csrf_exempt,name='dispatch')
class Save_pwd(View):
    def post(self,request):
        d2 = request.body
        d = json.loads(d2)
        try:
            res1 = MarchentModel.objects.get(Email_id=d['email_id'],password=d['old_pwd'])
            res1.password=d['new_pwd']
            res1.save()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)

    pass



