from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "portfolio/project1.html")

def project1_view(request):
    return render(request, "portfolio/project1.html")

def project2_view(request):
    return render(request, "portfolio/project3.html")

def project3_view(request):
    return render(request, "portfolio/project3.html")
