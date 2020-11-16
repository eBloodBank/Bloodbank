from django.urls import path,include
from . import views
from .views import (BloodBankListView, BloodBankDetailView, BloodBankCreateView, BloodBankUpdateView, BloodBankDeleteView, 
                    BloodDonationEventListView, BloodDonationEventCreateView, BloodPacketListView, BloodPacketDetailView,
                    UserOrderListView, DonationCreateView, UserDonationListView, DonationDetailView)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Blood Bank Mangement System API",
      default_version='v1',
      description="Get information about the Blood Banks, Blood Donors or Blood Donation Events for your city. You can filter the information by blood group or location.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.home, name='home'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('about/', views.about, name='about'),
    path('complete/', views.paymentComplete, name='complete'),
    path('bloodbanks/', BloodBankListView.as_view(), name='bloodbanks-list'),
    path('bloodbank/new/', BloodBankCreateView.as_view(), name='bloodbank-create'),
    path('bloodbank/<int:pk>', BloodBankDetailView.as_view(), name='bloodbanks-detail'),
    path('bloodbank/<int:pk>/update/', BloodBankUpdateView.as_view(), name='bloodbanks-update'),
    path('bloodbank/<int:pk>/delete/', BloodBankDeleteView.as_view(), name='bloodbanks-delete'), 
    path('bloodDonationEvents/', BloodDonationEventListView.as_view(), name='bloodDonationEvents-list'),
    path('bloodDonationEvent/new', BloodDonationEventCreateView.as_view(), name='bloodDonationEvents-create'),
    path('bloodPackets/', BloodPacketListView.as_view(), name='bloodpackets-list'),
    path('bloodPackets/<int:pk>', BloodPacketDetailView.as_view(), name='bloodpackets-detail'),
    path('orders/', UserOrderListView.as_view(), name='user-orders'),
    path('newDonation/', DonationCreateView.as_view(), name='donation-create'),
    path('donations/', UserDonationListView.as_view(), name='user-donations'),
    path('donation/<int:pk>', DonationDetailView.as_view(), name='donations-detail'),
]