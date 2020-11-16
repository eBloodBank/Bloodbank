from django.urls import path,include
from . import views
from website_pages import api_views as bb_views

urlpatterns = [
    path('donorData', views.donor_list_view, name='donor_list_view'),
    path('donorData/<int:pk>', views.donor_detail_view, name='donor_detail_view'),
    path('donorData/<slug:city>', views.donors_city, name='donors_city'),
    path('donorData/<slug:state>', views.donors_state, name='donors_state'),
    path('BloodBank/<slug:city>', bb_views.bloodbanks_city, name='bloodbanks_city'),
    path('BloodBank/<slug:state>', bb_views.bloodbanks_state, name='bloodbanks_state'),
]