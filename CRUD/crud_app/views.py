from django.shortcuts import render,redirect
from .models import *

def index(request):
  return render(request,"index.html")


def index(request):
  if(request.method=="POST"):
    data = request.POST
    image=request.FILES.get("image")
    name=data.get("name")
    email=data.get("email")
    age=data.get("age")
    
    
    
    UserIN.objects.create(
      name=name,
      email = email,
      age=age,
      image=image,
    )
    return redirect('/home/')
  queryset=UserIN.objects.all()
  context={'index':queryset}
  return render(request,"index.html",context)

def delete_index(request,id):
  queryset = UserIN.objects.get(id =id)
  queryset.delete()
  return redirect('/home/')


def update_index(request,id):
  queryset = UserIN.objects.get(id=id)
  if (request.method=="POST"):
    data = request.POST
    name=data.get("name")
    email=data.get("email")
    age=data.get("age")
    
    
    queryset.name=name
    queryset.email=email
    queryset.age=age
    
    queryset.save()
    return redirect('/home/')
    
  context = {'index':queryset}
  return render(request,"update_index.html",context)