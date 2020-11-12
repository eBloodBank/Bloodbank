from django.urls import path,include
from . import views

urlpatterns = [
    path('donorData', views.donor_list_view, name='donor_list_view'),
    path('donorData/<int:pk>', views.donor_detail_view, name='donor_detail_view'),

]