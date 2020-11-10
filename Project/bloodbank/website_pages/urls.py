from django.urls import path,include
from . import views
from .views import (BloodBankListView, BloodBankDetailView, BloodBankCreateView, BloodBankUpdateView, BloodBankDeleteView, 
                    BloodDonationEventListView, BloodDonationEventCreateView)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bloodbanks/', BloodBankListView.as_view(), name='bloodbanks-list'),
    path('bloodbank/new/', BloodBankCreateView.as_view(), name='bloodbank-create'),
    path('bloodbank/<int:pk>', BloodBankDetailView.as_view(), name='bloodbanks-detail'),
    path('bloodbank/<int:pk>/update/', BloodBankUpdateView.as_view(), name='bloodbanks-update'),
    path('bloodbank/<int:pk>/delete/', BloodBankDeleteView.as_view(), name='bloodbanks-delete'), 
    path('bloodDonationEvents/', BloodDonationEventListView.as_view(), name='bloodDonationEvent-list'),
    path('bloodDonationEvent/new', BloodDonationEventCreateView.as_view(), name='bloodDonationEvent-create'),
]