from django.shortcuts import render

def home(request):
    return render(request,'website_pages/home.html', {'title': 'Home Page'})

def about(request):
    return render(request,'website_pages/about.html', {'title': 'About Page'})
