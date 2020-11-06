from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:

    def test_bloodpacket_quantity_is_valid(self):
        bloodpacketz = mixer.blend('website_pages.BloodPacket', quantity=1)
        assert bloodpacketz.quantity_check == True

    def test_bloodpacket_quantity_is_invalid(self):
        bloodpacketz = mixer.blend('website_pages.BloodPacket', quantity=0)
        assert bloodpacketz.quantity_check == False