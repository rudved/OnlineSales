from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.
from django.views.generic.base import View


def mrtlogin(request):
    return render(request,'mrtlogin.html')

def login_check(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')
    d = {'email': uname, 'pwd': pwd}
    d2=json.dumps(d)
    res=requests.post('http://127.0.0.1:2000/check_login/',data=d2)
    return render(request,'merchant_home.html',{'data':res.json()})




def add_product(request):
    mid = request.GET['mid']
    return render(request,'add_product.html',{'data':mid})


def saveproduct(request):
    p_no = request.POST.get('p_no')
    p_name = request.POST.get('p_name')
    p_price = request.POST.get('p_price')
    p_qty = request.POST.get('p_qty')
    m_id = request.POST.get('m_id')
    data = {'p_no': p_no,'p_name':p_name,'p_price':p_price,'p_qty':p_qty,'m_id_id':m_id}
    json_data = json.dumps(data)
    print(json_data)
    res = requests.post('http://127.0.0.1:2000/saveproduct/',data=json_data)
    if (res.status_code)==200:
        msg = {"data saved"}
        return render(request,'merchant_home.html',{'msg':msg})


def viewproduct(request):
    mid = request.GET['mid']
    res = requests.get('http://127.0.0.1:2000/view_product/'+mid+'/')
    if res.status_code==200:
        return render(request,"view_product.html",{'data1':res.json()})


def update(request):
    p_no = request.GET.get('p_no')
    res = requests.get('http://127.0.0.1:2000/update/'+p_no+'/')
    if res.status_code==200:
        return render(request,'update.html',{'data2':res.json()})
    else:
        return HttpResponse('ERROR')


def update_p(request):
    p_no = request.POST.get('p_no')
    p_name = request.POST.get('p_name')
    p_price = request.POST.get('p_price')
    p_qty = request.POST.get('p_qty')
    data = {'p_no': p_no, 'p_name': p_name, 'p_price': p_price, 'p_quantity': p_qty}
    json_data = json.dumps(data)
    print(json_data)
    res = requests.put('http://127.0.0.1:2000/updateproduct/',data=json_data)
    print(res.status_code)
    if (res.status_code) == 200:
        msg = {"data updated"}
        return render(request, 'merchant_home.html', {'msg': msg})


def delete(request):
    p_no = request.GET['p_no']
    res = requests.delete('http://127.0.0.1:2000/delete/'+p_no+'/')
    if (res.status_code) == 200:
        msg = {"Product Delete"}
        return render(request, 'merchant_home.html', {'msg': msg})


def logout(request):
    return render(request,'mrtlogin.html')


def change_pwd(request):
    return render(request,'changepassword.html')


def save_pwd(request):
    email_id = request.POST['email_id']
    old_pwd = request.POST['old_pwd']
    new_pwd = request.POST['new_pwd']
    confirm_pwd = request.POST['confirm_pwd']
    if new_pwd == confirm_pwd:
        d1 = {'email_id':email_id,'old_pwd':old_pwd,'new_pwd':new_pwd}
        json_data = json.dumps(d1)
        print(json_data)
        res = requests.post('http://127.0.0.1:2000/save_pwd/',data=json_data)
        if res.status_code==200:
            msg = {'password changed sucesfully'}
            return render(request, 'merchant_home.html', {'msg': msg})
        else:
            return render(request,'changepassword.html',{'msg':'Given Email_Id and Password is Invalied'})
    else:
        return render(request,'changepassword.html',{'msg':'new password and confirm password is not matched'})