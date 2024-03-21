from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.
def teacherregister(request):
    if request.method=='POST':
        u=User.objects.filter(username=request.POST['username'])
        if u.exists():
            messages.info(request,'username already taken')
            return redirect('myapp:teacherr')
        form=teacherregForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('myapp:teacherl'))
    f=teacherregForm()
    return render(request,'teacherregister.html',context={'form':f})

def teacherlogin(request):
    if request.method=='POST':
        form=teacherlogForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect(reverse('myapp:teachersr'))
            else:
                messages.info(request,'invalid user')
                return redirect(reverse('myapp:teacherl'))
    f=teacherlogForm()
    return render(request,'teacherlogin.html',context={'form':f})


def home(request):
    return render(request,'frontpage.html')

@login_required(login_url='myapp:teacherl')
def teachers(request):
    if request.method=='POST':
        form=teachersrForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('myapp:teacherdata'))
    f=teachersrForm()
    return render(request,'teacherform.html',context={'form':f})
@login_required(login_url='myapp:teacherl')
def course(request):
    data=courses.objects.all()
    info={'data':data}
    return render(request,'course.html',context=info)

@login_required(login_url='myapp:teacherl')
def teacherdata(request):
    data=teachersrModel.objects.all()
    info={'data':data}
    return render(request,'teacherdata.html',context=info)

@login_required(login_url='myapp:teacherl')
def payment(request):
    return render(request,'payments.html')

def logout_view(request):
      logout(request)
      return redirect(reverse('myapp:teacherl'))
@login_required(login_url='myapp:teacherl')
def students(request):
    if request.method=='POST':
        form=studentsrForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('myapp:studentdata'))
    f=studentsrForm()
    return render(request,'studentform.html',context={'form':f})
@login_required(login_url='myapp:teacherl')
def studentdata(request):
    data=studentsrModel.objects.all()
    info={'data':data}
    return render(request,'studentdata.html',context=info)


def enquiryview(request):
    return render(request,'enquiry.html')

