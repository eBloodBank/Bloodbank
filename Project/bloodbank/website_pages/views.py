from django.shortcuts import render,get_object_or_404,redirect
from .models import BloodBank, BloodPacket, BloodDonationEvent, Order, Donation
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms.models import inlineformset_factory
from django.urls import reverse
import json
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    return render(request,'website_pages/home.html', {'title': 'Home Page'})

def about(request):
    return render(request,'website_pages/about.html', {'title': 'About Page'})

class BloodPacketListView(ListView):
    model = BloodPacket
    template_name = 'website_pages/bloodpacketlist.html'
    context_object_name = 'bloodpackets'

    def get_queryset(self): # new
        bloodgroupz = self.request.GET.get('bloodgroupz')
        
        if bloodgroupz is None:
            object_list = BloodPacket.objects.all()
            return object_list

        if bloodgroupz is "":
            object_list = BloodPacket.objects.all()
            return object_list
        if bloodgroupz not in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']:
            object_list = BloodPacket.objects.filter(bloodGroup='invalid')
            return object_list
            
        bg = next(filter(lambda x: x[1]==bloodgroupz, BloodPacket.BLOOD_GROUPS))
        print(bg)

        object_list = BloodPacket.objects.filter(bloodGroup=bg[0])
        return object_list

class BloodPacketDetailView(DetailView):
    model = BloodPacket

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
        return reverse('bloodDonationEvents-list')

class BloodBankListView(ListView):
    model = BloodBank
    template_name = 'website_pages/bloodbanklist.html'
    context_object_name = 'bloodbanks'

    def get_queryset(self): # new
        cityz = self.request.GET.get('cityz')
        if cityz is None:
            object_list = BloodBank.objects.all()
            return object_list

        object_list = BloodBank.objects.filter(city=cityz)
        return object_list
    
class BloodBankDetailView(DetailView):
    model = BloodBank

BloodPacketFormset = inlineformset_factory(BloodBank, BloodPacket, fields=('packetID', 'bloodGroup', 'expiryDate', 'quantity', 'price'))
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
        return reverse('bloodbanks-list')

class BloodBankUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BloodBank
    fields = ['name', 'district', 'city', 'state', 'category', 'contactNo', 'email', 'PostalAddress' ]
    template_name = 'website_pages/BloodBank_form.html'
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
        return reverse('bloodbanks-list')

class BloodBankDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BloodBank
    success_url = '/'

    def test_func(self):
        BloodBankz = self.get_object()
        if self.request.user == BloodBankz.BloodBankAdmin:
            return True
        return False

def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY', body)
    bloodpacket = BloodPacket.objects.get(pk=body['packetpk'])
    Order.objects.create(packetID=bloodpacket.packetID, bloodBank=bloodpacket.Blood_bank
    , boughtBy=request.user, amount = bloodpacket.price)
    bloodpacket.delete()
    return JsonResponse('Payment Completed', safe=False)

class UserOrderListView(ListView, LoginRequiredMixin):
    model = Order
    template_name = 'website_pages/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):     # Return trips of a specific user 
        user = self.request.user
        return Order.objects.filter(boughtBy=user)
    
class DonationCreateView(LoginRequiredMixin, CreateView): # Creating a trip Logic 
    model = Donation
    fields = ['bloodBank','date']

    def form_valid(self,form):
        form.instance.donor = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('user-donations')
    
class UserDonationListView(ListView, LoginRequiredMixin):
    model = Donation
    template_name = 'website_pages/donations.html'
    context_object_name = 'donations'

    def get_queryset(self):     # Return trips of a specific user 
        user = self.request.user
        return Donation.objects.filter(donor=user)
    
class DonationDetailView(DetailView):
    model = Donation