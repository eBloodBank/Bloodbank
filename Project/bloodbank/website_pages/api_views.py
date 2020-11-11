from rest_framework import viewsets
from .models import BloodBank, BloodPacket, BloodDonationEvent
from user.models import User
from rest_framework.response import Response
from .serializers import BloodBankSerializer, UserSerializer, BloodPacketSerializer, BloodDonationEventSerializer
from rest_framework import status

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
    http_method_names = ["get",'post']
    queryset = BloodDonationEvent.objects.all()
    serializer_class = BloodDonationEventSerializer



