from django.urls import reverse, resolve

class TestUrls:

    def test_detail_url_bb(self):
        path = reverse('bloodbank-detail', kwargs={'pk': 39})
        assert resolve(path).view_name == 'bloodbank-detail'

    def test_detail_url_bp(self):
        path = reverse('bloodpackets-detail', kwargs={'pk': 39})
        assert resolve(path).view_name == 'bloodpackets-detail'
    
    def test_detail_url_bd(self):
        path = reverse('donations-detail', kwargs={'pk': 3})
        assert resolve(path).view_name == 'donations-detail'

    def test_detail_url_bb_update(self):
        path = reverse('bloodbanks-update', kwargs={'pk': 39})
        assert resolve(path).view_name == 'bloodbanks-update'
    
    def test_detail_url_bb_delete(self):
        path = reverse('bloodbanks-delete', kwargs={'pk': 39})
        assert resolve(path).view_name == 'bloodbanks-delete'
    
    def test_detail_url_bb_create(self):
        path = reverse('bloodbank-create')
        assert resolve(path).view_name == 'bloodbank-create'

    def test_detail_url_home(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_detail_url_about(self):
        path = reverse('about')
        assert resolve(path).view_name == 'about'

    def test_detail_url_complete(self):
        path = reverse('complete')
        assert resolve(path).view_name == 'complete'