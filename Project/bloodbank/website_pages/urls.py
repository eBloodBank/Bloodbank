from django.urls import path,include
from . import views
from .views import BloodBankListView, BloodBankDetailView, BloodBankCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bloodbanks/', BloodBankListView.as_view(), name='bloodbank-list'),
    path('bloodbank/new/', BloodBankCreateView.as_view(), name='bloodbank-create'),
    path('bloodbank/<int:pk>', BloodBankDetailView.as_view(), name='bloodbank-detail'),
]