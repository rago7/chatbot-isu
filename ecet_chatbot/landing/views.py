from django.http import HttpResponse
from django.shortcuts import render
HttpResponse
# Create your views here.
def simpleLanding(req):
    return HttpResponse("<h1>Hello !!! Landing Page !!</h1>")

def startPage(req):
    return render(req, 'landing/landing.html')
