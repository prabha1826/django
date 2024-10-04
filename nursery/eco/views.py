from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators  import login_required
# Create your views here.

def home(request):
    #return HttpResponse(
    #"""
    #<h1 style="text-align:center"> Hello Welcome to Nursery</h1>
    #<h5>See all the Available species</h5>
    #<p style="text-align:right">Select your likes from below</p>
    #<img src="" alt="image">
    #"""
    #)
    plants=[
        {'name':'Rose','Price':100},
        {'name':'Lilly','Price':100},
        {'name':'Crysanthemum','Price':100},
        {'name':'Tulip','Price':100},
    ]
    message="Wonder world of Green"
    return render(request, "home.html",context={"plants":plants,"msg":message})
    #return render(request,"nursery.html")

def nursery(request):
    plants=[
        {'name':'Rose','Price':100},
        {'name':'Lilly','Price':99},
        {'name':'Crysanthemum','Price':70},
        {'name':'Tulip','Price':40},
    ]
    return render(request,"nursery.html",context={"plants":plants})

def contacts(request):
    return render(request,"contacts.html")

@login_required(login_url="/login/")

def add_plant(request):
    if  request.method == "POST":
        data = request.POST
        plant_name=data.get('plant_name')
        scientific_name=data.get('scientific_name')
        price=int(data.get('price'))
        age=int(data.get('age'))
        pic=request.FILES.get("pic")
        imported=data.get('imported') == 'on'
        
        #create a new plant record
        Plant.objects.create(
            plant_name=plant_name,
            scientific_name=scientific_name,
            price=price,
            age=age,
            pic=pic,
            imported=imported
        )
        
        #Display success toast message
        messages.success(request,"Plant added successfully")
    
    return render(request,"add_plant.html")


# 2. Get all plants
def all_plants(request):
    plants = Plant.objects.all()
    return render(request, 'all_plants.html', {'plants': plants})

# 3. Delete a particular plant
def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    plant.delete()
    messages.success(request, "Plant deleted successfully")
    return redirect('plant_list')

# 4. Update a particular plant
def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    
    if request.method == "POST":
        plant.plant_name = request.POST.get('plant_name')
        plant.scientific_name = request.POST.get('scientific_name')
        plant.price = int(request.POST.get('price'))
        plant.age = int(request.POST.get('age'))
        plant.imported = request.POST.get('imported') == 'on'
        
        if request.FILES.get("pic"):
            plant.pic = request.FILES.get("pic")

        plant.save()
        messages.success(request, "Plant updated successfully")
        return redirect('all_plants')
    
    return render(request, "update_plants.html", {'plant': plant})

# Login view
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username!")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, "Invalid Password!")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')
    return render(request, "login.html")

# Logout view
def logout_page(request):
    logout(request)
    return redirect('/login/')

# Register view
def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, 'Username already exists! Please try another one.')
            return redirect('/register/')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)  # hashing the password
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('/login/')
    
    return render(request, "register.html")