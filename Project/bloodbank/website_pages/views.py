from django.shortcuts import render
from .models import BloodBank, BloodPacket, BloodDonationEvent
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms.models import inlineformset_factory
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    return render(request,'website_pages/home.html')

def about(request):
    return render(request,'website_pages/about.html')

class BloodDonationEventListView(ListView):
    model = BloodDonationEvent
    template_name = 'website_pages/blooddonationlist.html'
    context_object_name = 'bloodDonationEvents'
    ordering = ['date']

class BloodDonationEventCreateView(LoginRequiredMixin, CreateView):
    model = BloodDonationEvent
    fields = ['date', 'venue', 'time', 'campName', 'state', 'district', 'contactNo']
    
    def form_valid(self, form):
        userz = self.request.user
        BloodBankz = BloodBank.objects.filter(BloodBankAdmin=userz).first()
        form.instance.organizedBy = BloodBankz
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('bloodDonationEvent-list')

class BloodBankListView(ListView):
    model = BloodBank
    template_name = 'website_pages/bloodbanklist.html'
    context_object_name = 'bloodbanks'
    
class BloodBankDetailView(DetailView):
    model = BloodBank

BloodPacketFormset = inlineformset_factory(BloodBank, BloodPacket, fields=('packetID', 'bloodGroup', 'expiryDate', 'quantity'))
class BloodBankCreateView(LoginRequiredMixin, CreateView):
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

class BloodBankUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BloodBank
    fields = ['name', 'district', 'city', 'state', 'category', 'contactNo', 'email', 'PostalAddress' ]

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered.
        # the difference with CreateView is that
        # on this view we pass instance argument
        # to the formset because we already have
        # the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["BloodPacketz"] = BloodPacketFormset(self.request.POST, instance=self.object)
        else:
            data["BloodPacketz"] = BloodPacketFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        BloodPacketz = context["BloodPacketz"]
        self.object = form.save()
        if BloodPacketz.is_valid():
            BloodPacketz.instance = self.object
            BloodPacketz.save()
        setz = BloodPacket.objects.filter(Blood_bank = form.instance)
        form.instance.BloodPackets.add(*setz)
        return super().form_valid(form)
    
    def test_func(self):
        BloodBankz = self.get_object()
        if self.request.user == BloodBankz.BloodBankAdmin:
            return True
        return False

    def get_success_url(self):
        return reverse('bloodbank-list')

class BloodBankDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BloodBank
    success_url = '/'

    def test_func(self):
        BloodBankz = self.get_object()
        if self.request.user == BloodBankz.BloodBankAdmin:
            return True
        return False

