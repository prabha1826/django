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
    return render(request, "home.html")
