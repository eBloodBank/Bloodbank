from rest_framework import routers
from website_pages import api_views

router = routers.DefaultRouter()
router.register(r'BloodBank', api_views.BloodBankViewSet)
router.register(r'BloodPacket', api_views.BloodPacketViewSet)
