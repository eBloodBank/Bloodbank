"""bloodbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as account_views
<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.contrib.auth import views as auth_views
>>>>>>> aace3631055419c5f23a76a15f0f8885fcdb04b1
=======
from django.contrib.auth import views as auth_views

>>>>>>> ae8549cb95ee91a77bff14946a051b81f0fb60a8


urlpatterns = [
    path('', include('website_pages.urls')),
    path('admin/', admin.site.urls),
    path('register/', account_views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]
