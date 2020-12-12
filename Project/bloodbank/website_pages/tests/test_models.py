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
    
    def test_bb_str(self):
        bloodbankz = mixer.blend('website_pages.BloodBank',name = "testing")
        assert str(bloodbankz)== bloodbankz.name
    
    def test_bp_str(self):
        bloodpacketz = mixer.blend('website_pages.BloodPacket',packetID = '1234')
        assert str(bloodpacketz)==bloodpacketz.packetID
    
    def test_be_str(self):
        bloodcampz = mixer.blend('website_pages.BloodDonationEvent',campName = "testing")
        assert str(bloodcampz)== bloodcampz.campName
    
    def test_order_str(self):
        orderz = mixer.blend('website_pages.Order',packetID = '1234')
        assert str(orderz)== orderz.packetID

    def test_usr_short_name(self):
        usez = mixer.blend('user.User', first_name="utkarsh", last_name="aditya")
        assert usez.get_short_name() == "utkarsh"

    def test_usr_full_name(self):
        usez = mixer.blend('user.User', first_name="utkarsh", last_name="aditya")
        assert usez.get_full_name() == "utkarsh aditya"