from rest_framework import viewsets
from .models import BloodBank, BloodPacket, BloodDonationEvent
from user.models import User
from rest_framework.response import Response
from .serializers import BloodBankSerializer, UserSerializer, BloodPacketSerializer, BloodDonationEventSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema('GET', responses = {200: BloodBankSerializer(many=True)}, operation_summary="Get City Filtered Bloodbanks", operation_id="bloodbanks_city" )
@api_view(http_method_names=['GET']) #manages the request in a way that is useable by other rest frameworks
def bloodbanks_city(request, city):
    data = BloodBank.objects.filter(city=city)
    serializer = BloodBankSerializer(data, many=True)
    return Response(data=serializer.data)

@swagger_auto_schema('GET', responses = {200: BloodBankSerializer(many=True)}, operation_summary="Get State Filtered Bloodbanks",operation_id="bloodbanks_state" )
@api_view(http_method_names=['GET']) #manages the request in a way that is useable by other rest frameworks
def bloodbanks_state(request, state):
    data = BloodBank.objects.filter(state=state)
    serializer = BloodBankSerializer(data, many=True)
    return Response(data=serializer.data)

class BloodBankViewSet(viewsets.ModelViewSet):
    queryset = BloodBank.objects.all()
    serializer_class = BloodBankSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if request.user.pk != instance.BloodBankAdmin.pk:
            data={'message' : "You Cannot update some other Blood Bank's data"}
            return Response(data)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.pk != instance.BloodBankAdmin.pk:
            data={'message' : "You Cannot delete some other Blood Bank's data"}
            return Response(data)
        self.perform_destroy(instance)
        data={'message' : "Deleted Successfully"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)

class BloodPacketViewSet(viewsets.ModelViewSet):
    queryset = BloodPacket.objects.all()
    serializer_class = BloodPacketSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BloodDonationEventViewSet(viewsets.ModelViewSet):
    queryset = BloodDonationEvent.objects.all()
    serializer_class = BloodDonationEventSerializer



