from django.shortcuts import render
from .models import BloodBank, BloodPacket
from django.views.generic import ListView, DetailView, CreateView
from django.forms.models import inlineformset_factory
from django.urls import reverse


def home(request):
    return render(request,'website_pages/home.html')

def about(request):
    return render(request,'website_pages/about.html')

class BloodBankListView(ListView):
    model = BloodBank
    template_name = 'website_pages/bloodbanklist.html'
    context_object_name = 'bloodbanks'
    
class BloodBankDetailView(DetailView):
    model = BloodBank

BloodPacketFormset = inlineformset_factory(BloodBank, BloodPacket, fields=('packetID', 'bloodGroup', 'expiryDate', 'quantity'))
class BloodBankCreateView(CreateView):
    model = BloodBank    
    fields = ['name', 'district', 'city', 'state', 'category', 'contactNo', 'email', 'PostalAddress' ]

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["BloodPacketz"] = BloodPacketFormset(self.request.POST)
        else:
            data["BloodPacketz"] = BloodPacketFormset()
        return data

    def form_valid(self, form):
        form.instance.BloodBankAdmin = self.request.user
        context = self.get_context_data()
        BloodPacketz = context["BloodPacketz"]
        self.object = form.save()
        a = self.object
        if BloodPacketz.is_valid():
            BloodPacketz.instance = self.object
            BloodPacketz.save()
        setz = BloodPacket.objects.filter(Blood_bank = form.instance)
        form.instance.BloodPackets.add(*setz)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bloodbank-list')

