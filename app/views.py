from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from app.models import *
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from app.serializers import *

from rest_framework.response import Response
from django.views.generic import CreateView

def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d={'username':username}

        return render(request,'home.html',d)
    return render(request,'home.html')


def Register(request):
    UFO = UserForm()
    d={'UFO':UFO}
    if request.method == 'POST':
        UFO = UserForm(request.POST)
        if UFO.is_valid():
            NUFO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NUFO.set_password(password)
            NUFO.save()
            return HttpResponse("Registration is done successfully")

    return render(request,'register.html',d)


def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('username or password is Invalid')
    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



@login_required
def insert_data(request):
    d={'LFO':LaptopForm()}
    if request.method =='POST' and request.FILES:
        LO=LaptopForm(request.POST,request.FILES)
        if LO.is_valid():
            LO.save()
            return HttpResponse("The data is inserted successfully")
        else:
            return HttpResponse("The data is not valid")
    return render(request,'insert_data.html',d)


class LaptopsData(viewsets.ViewSet):
    def list(self,request):
        LQS=Laptops.objects.all()
        SJD=LaptopsMS(LQS,many=True)
        d={'data':SJD.data}
        return render(request,'list.html',d)

    def retrieve(self,request,pk):
        LO=Laptops.objects.get(pk=pk)
        SDO=LaptopsMS(LO)
        return Response(SDO.data)

    def update(self,request,pk):
        SLO=Laptops.objects.get(pk=pk)
        SLD=LaptopsMS(SLO,data=request.data)
        if SLD.is_valid():
            SLD.save()
            return Response({'Updated':'Laptop is updated'})
        else:
            return Response({'Failed':'Laptop is Not Updated'})
    
    def partial_update(self,request,pk):
        SLO=Laptops.objects.get(pk=pk)
        SLD=LaptopsMS(SLO,data=request.data,partial=True)
        if SLO.is_valid():
            SLO.save()
            return Response({'Updated':'Laptop is updated'})
        else:
            return Response({'Failed':'Laptop is Not Updated'})
        

    def destroy(self,request,pk):
        Laptops.objects.get(pk=pk).delete()
        return Response({'Deleted':'Laptop is deleted'})


    




