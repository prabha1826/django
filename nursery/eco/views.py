from django.shortcuts import render
from django.http import HttpResponse
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
    #return render(request, "home.html",context={"plants":plants,"msg":message})
    return render(request,"nursery.html")