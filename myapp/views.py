from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
def index(request):
    return render(request,"index.html")
def register(request):
    return render(request,'register.html')
def registerAction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    place=request.POST['place']
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb(Name=name,Adress=address,Gender=gender,Place=place,Username=username,Password=password)
    user.save()
    messages.add_message(request,messages.INFO,"Registration was suucessfull")
    return redirect("register")
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb.objects.filter(Username=username,Password=password)
    if(user.count()>0):
        request.session["id"]=user[0].id
        return render(request,'userhome.html')
    else:
        return redirect("index")
        messages.add_message(request,messages.INFO,"Invalid username or password")
        
def viewuser(request):
    user=register_tb.objects.all()
    return render(request,'viewuser.html',{'vi':user})
def edit(request,id):
    user=register_tb.objects.filter(id=id)
    return render(request,'edit.html',{'ed':user})
def editAction(request):
    id=request.POST['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    place=request.POST['place']
    username=request.POST['username']
    password=request.POST['password']
    edit=register_tb.objects.filter(id=id).update(Name=name,Adress=address,Gender=gender,Place=place,Username=username,Password=password)
    return redirect("viewuser")
def delete(request,id):
    register_tb.objects.filter(id=id).delete()
    return redirect("viewuser")
def uploadfile(request):
    return render(request,'uploadfile.html')
def uploadAction(request):
    if len(request.FILES)>0:
        img=request.FILES['image']
    else:
        img="no pic"
    image=image_tb(file=img)
    image.save()
    return redirect("uploadfile")
def viewImage(request):
    image=image_tb.objects.all()
    return render(request,'viewImage.html',{'im':image})
def viewCountry(request):
    country=country_tb.objects.all()
    return render(request,'viewCountry.html',{'co':country})
def getstate(request):
    countryid=request.GET['co']
    state=state_tb.objects.filter(Country_id_id=countryid)
    return render(request,'getstate.html',{'st':state})
def hidefunction(request):
    return render(request,'hidefunction.html')
def mouseevents(request):
    return render(request,'mouseevents.html')
def checkuser(request):
    user=request.GET['us']
    username=register_tb.objects.filter(Username=user)
    if(username.count()>0):
        msg='exist'
    else:
        msg='notexist'
    return JsonResponse({'valid':msg})


    