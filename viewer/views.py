from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView
from django.views import View
from django.views.generic import TemplateView, ListView

from viewer.forms import ApartmentModelForm, GroundModelForm, HouseModelForm, AuctionModelForm, PropertyTypeModelForm
from viewer.models import House, Apartment, PropertyType
from logging import getLogger
from viewer.models import House, Apartment, Ground, Auction

LOGGER = getLogger()

def home(request):
    return render(request, "home.html")


def houses(request):
    houses_ = House.objects.all()
    context = {'houses': houses_}
    return render(request, 'houses.html', context)

def house(request, pk):
    if House.objects.filter(id=pk).exists():
        house_ = House.objects.get(id=pk)
        context = {'house': house_}
        return render(request, 'house.html', context)
    return grounds(request)


class HousesView(View):
    def get(self, request):
        houses_ = House.objects.all()
        context = {'houses': houses_}
        return render(request, "houses.html", context)


class HousesTemplateView(TemplateView):
    template_name = "houses.html"
    extra_context = {'houses': House.objects.all()}


class HousesListView(ListView):
    template_name = "houses.html"
    model = House
    context_object_name = 'houses'

def apartments(request):
    apartments_ = Apartment.objects.all()
    context = {'apartments': apartments_}
    return render(request, 'apartments.html', context)


def insert_data(request):
    return render(request, "insert_data.html")


class InsertHouse(CreateView):
    template_name = 'form.html'
    form_class = HouseModelForm
    success_url = reverse_lazy('insert_property_type')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)


class UpdateHouse(UpdateView):
    template_name = 'form.html'
    form_class = HouseModelForm
    success_url = reverse_lazy('houses')
    model = House

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)


class InsertApartments(CreateView):
    template_name = "form.html"
    form_class = ApartmentModelForm
    success_url = reverse_lazy('insert_property_type')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class UpdateApartments(UpdateView):
    template_name = 'form.html'
    form_class = ApartmentModelForm
    success_url = reverse_lazy('apartments')
    model = Apartment

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)


class InsertGrounds(CreateView):
    template_name = "form.html"
    form_class = GroundModelForm
    success_url = reverse_lazy('insert_property_type')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class UpdateGrounds(UpdateView):
    template_name = 'form.html'
    form_class = GroundModelForm
    success_url = reverse_lazy('grounds')
    model = Ground

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)


class InsertPropertytype(CreateView):
    template_name = "form.html"
    form_class = PropertyTypeModelForm
    success_url = reverse_lazy('insert_auction')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)


class InsertAuction(CreateView):
    template_name = "form.html"
    form_class = AuctionModelForm
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class UpdateAuction(UpdateView):
    template_name = 'form.html'
    form_class = AuctionModelForm
    success_url = reverse_lazy('auctions')
    model = Auction

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)



def apartment(request, pk):
    if Apartment.objects.filter(id=pk).exists():
        apartment_ = Apartment.objects.get(id=pk)
        context = {'apartment': apartment_}
        return render(request, 'apartment.html', context)
    return grounds(request)


class ApartmentsView(View):
    def get(self, request):
        apartments_ = Apartment.objects.all()
        context = {'apartments': apartments_}
        return render(request, "apartments.html", context)


class ApartmentsTemplateView(TemplateView):
    template_name = "apartments.html"
    extra_context = {'apartments': Apartment.objects.all()}


class ApartmentsListView(ListView):
    template_name = "apartments.html"
    model = Apartment
    context_object_name = 'apartments'


def grounds(request):
    grounds_ = Ground.objects.all()
    context = {'grounds': grounds_}
    return render(request, 'grounds.html', context)

def ground(request, pk):
    if Ground.objects.filter(id=pk).exists():
        ground_ = Ground.objects.get(id=pk)
        context = {'ground': ground_}
        return render(request, 'ground.html', context)
    return grounds(request)


class GroundsView(View):
    def get(self, request):
        grounds_ = Ground.objects.all()
        context = {'grounds': grounds_}
        return render(request, "grounds.html", context)


class GroundsTemplateView(TemplateView):
    template_name = "grounds.html"
    extra_context = {'grounds': Ground.objects.all()}


class GroundsListView(ListView):
    template_name = "grounds.html"
    model = Ground
    context_object_name = 'grounds'


def auctions(request):
    auctions_ = Auction.objects.all()
    context = {'auctions': auctions_}
    return render(request, 'auctions.html', context)

def auction(request, pk):
    if Auction.objects.filter(id=pk).exists():
        auction_ = Auction.objects.get(id=pk)
        context = {'auction': auction_}
        return render(request, 'auction.html', context)
    return grounds(request)


class AuctionView(View):
    def get(self, request):
        auctions_ = Auction.objects.all()
        context = {'auctions': auctions_}
        return render(request, "auctions.html", context)


class AuctionsTemplateView(TemplateView):
    template_name = "auctions.html"
    extra_context = {'auctions': Auction.objects.all()}


class AuctionsListView(ListView):
    template_name = "auctions.html"
    model = Auction
    context_object_name = 'auctions'
