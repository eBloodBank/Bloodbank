from django.urls import reverse, resolve

class TestUrls:

    def test_detail_url(self):
        path = reverse('bloodbank-detail', kwargs={'pk': 39})
        assert resolve(path).view_name == 'bloodbank-detail'