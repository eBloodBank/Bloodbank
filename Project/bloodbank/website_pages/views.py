from django.shortcuts import render

def home(request):
    return render(request,'website_pages/home.html')

def about(request):
    return render(request,'website_pages/about.html')
