from rest_framework import status #tells whether successful or not(404)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User
from .serializers import DonorSerializer
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema

#packages appropiately the request for function based view
@swagger_auto_schema('GET', responses = {200: DonorSerializer(many=True)}, operation_summary="Get list of Donors" )
@swagger_auto_schema('POST', request_body = DonorSerializer, responses={200: "Successfully Registered", 404: "Bad Request" }, operation_summary="Create New Donor")
@api_view(http_method_names=['GET','POST']) #manages the request in a way that is useable by other rest frameworks
def donor_list_view(request):
    if request.method == 'GET':
        return donor_list_view_get(request)
    elif request.method == 'POST':
        return donor_view_post(request)

def donor_list_view_get(request):
    try:
        data = User.objects.all()
        serializer = DonorSerializer(data, many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def donor_view_post(request):
    password = request.data.get('password')
    donor = User()
    donor.set_password(password)
    serializer = DonorSerializer(donor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        data={'message' : "Successfully Registered"}
        return Response(data, status = status.HTTP_200_OK)
    else:
        return Response(serializer.errors ,status = status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema('GET', responses = {200: DonorSerializer, 404: "Donor Doesn't Exist" } )
@api_view(http_method_names=['GET','PUT','DELETE']) #manages the request in a way that is useable by other rest frameworks
def donor_detail_view(request, pk):
    try:
        donor = User.objects.get(pk=pk)
        if request.method == 'GET':
            return donor_detail_view_get(request, pk, donor)
        elif request.method == 'PUT':
            return donor_detail_put(request, pk, donor)
        elif request.method == 'DELETE':
            return donor_detail_delete(request, pk, donor)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def donor_detail_view_get(request, pk, donor):
    serializer = DonorSerializer(donor)
    return Response(serializer.data)

def donor_detail_put(request, pk, donor):
    serializer = DonorSerializer(donor, data=request.data)
    if request.user.pk == pk:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors ,status = status.HTTP_400_BAD_REQUEST)
    else:
        data={'message' : "You Cannot update some other donor's data"}
        return Response(data)

def donor_detail_delete(request, pk, donor):
    if request.user.pk == pk:
        donor.delete()
        data={'message' : 'Successfully Deleted User'}
        return Response(data)
    else:
        data={'message' : "You Cannot delete some other donor's data"}
        return Response(data)

    