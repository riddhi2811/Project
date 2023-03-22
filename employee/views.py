
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import employee_data
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request,'login.html')

@login_required
def content(request):
    data_1=employee_data.objects.all()
    return render(request,'index.html',{'data_1':data_1})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        val={'username':username}
        error_Msg=''
        if (not username):
            error_Msg="User name is Required"
        elif len(username)<=2:
            error_Msg="User name should be of minimum 3 letters"
        elif (not password):
            error_Msg="Password is Required"
        if user is not None:
            login(request,user) 
            messages.success(request, "Successfully Logged In")
            return redirect('content')
        else:
            data={
                'error_message': error_Msg,
                'vals':val
                }
            return render(request, 'login.html', data)
    return render(request, 'login.html')

def filt(request):
    if request.method == 'POST':
        fromdate = request.POST['fromdate']
        print(fromdate)
        to = request.POST['to']
        print(to)
        m=employee_data.objects.filter(date__lte=to,date__gte=fromdate)
        return render(request,'response.html',{'m':m})
    return render(request,'index.html')

# def sea(request):
#     if request.method == 'POST':
#         name = request.POST['fname']
#         v=employee_data.objects.filter(name)
#         return render(request,'name_response.html',{'v':v})
#     return render(request,'index.html')

# @csrf_exempt
# def range(request): 
#     if request.method == 'POST':
#         From = request.POST.get('From')
#         to = request.POST.get('to')
#         print(From)
#         print(to)
#         query = "SELECT * from employee_data WHERE date BETWEEN '{From}' AND '{to}'"
#     return render(request,'content', {'data_2':query})



# import csv
# def export(response):
#     l1 = employee_data.objects.all()
#     response = HttpResponse('text/csv')
#     response['Content-Disposition']= 'attachment;filename="employee.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['Employee Id','First Name','Date','Check-In','Check-Out'])
#     l2=l1.values_list('Emp_id','Emp_name','date','check_in','check_out')
#     for emp in l2:
#         writer.writerow(emp)
#     return response



