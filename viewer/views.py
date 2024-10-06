from datetime import datetime, tzinfo
from lib2to3.fixes.fix_input import context

import pytz

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, TemplateView, ListView, CreateView, DetailView
from django.views import View

from accounts.models import Profile
from viewer.forms import ImageModelForm, BidModelForm, CitiesModelForm, HouseTypeModelForm, ApartmentTypeModelForm, GroundTypeModelForm, BidModelForm, ImageModelForm, ApartmentModelForm, GroundModelForm, HouseModelForm, AuctionModelForm, PropertyTypeModelForm
from viewer.models import House, Apartment, Ground, Auction, Image, Bid, HouseType, ApartmentType, Cities, GroundType

from logging import getLogger

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

def house_types(request):
    house_types = HouseType.objects.all()
    context = {'house_types': house_types}
    return render(request, 'house_types.html', context)

class HousesView(View):
    def get(self, request):
        houses_ = House.objects.all()
        context = {'houses': houses_}
        return render(request, "houses.html", context)


class HousesTemplateView(TemplateView):
    template_name = "houses.html"
    extra_context = {'houses': House.objects.all()}

class HouseTypesListView(ListView):
    template_name = "house_types.html"
    model = HouseType
    context_object_name = 'house_types'

class DeleteHouseType(DeleteView):
    template_name = 'confirm_delete.html'
    model = HouseType
    success_url = reverse_lazy('insert_data')

class HousesListView(ListView):
    template_name = "houses.html"
    model = House
    context_object_name = 'houses'

class InsertDataListView(PermissionRequiredMixin, ListView):
    template_name = "insert_data.html"
    model = Auction
    context_object_name = 'insert_data'
    permission_required = 'viewer.insert_data'

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

class DeleteHouse(DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = House
    success_url = reverse_lazy('houses')


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

class DeleteApartments(DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = Apartment
    success_url = reverse_lazy('apartments')


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

class DeleteGrounds(DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = Ground
    success_url = reverse_lazy('grounds')


class InsertPropertyType(CreateView):
    template_name = "form.html"
    form_class = PropertyTypeModelForm
    success_url = reverse_lazy('insert_auction')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)


class InsertAuction(CreateView):
    template_name = "form.html"
    form_class = AuctionModelForm
    success_url = reverse_lazy('image_create')

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

class DeleteAuction(DeleteView):
    template_name = 'confirm_delete.html'
    model = Auction
    success_url = reverse_lazy('auctions')

class InsertBid(CreateView):
    model = Bid
    template_name = "auction.html"
    form_class = BidModelForm
    success_url = reverse_lazy('auction')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

def apartment(request, pk):
    if Apartment.objects.filter(id=pk).exists():
        apartment_ = Apartment.objects.get(id=pk)
        context = {'apartment': apartment_}
        return render(request, 'apartment.html', context)
    return apartments(request)

def apartments(request):
    apartments_ = Apartment.objects.all()
    context = {'apartments': apartments_}
    return render(request, 'apartments.html', context)

def aparment_types(request):
    apartment_types_ = ApartmentType.objects.all()
    context = {'apartment_types': apartment_types_}
    return render(request, 'apartment_types.html', context)

class ApartmentsView(View):
    def get(self, request):
        apartments_ = Apartment.objects.all()
        context = {'apartments': apartments_}
        return render(request, "apartments.html", context)

class DeleteApartmentType(DeleteView):
    template_name = 'confirm_delete.html'
    model = ApartmentType
    success_url = reverse_lazy('insert_data')


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

def ground_types(request):
    ground_types_ = GroundType.objects.all()
    context = {'ground_types': ground_types_}
    return render(request, 'ground_types.html', context)

class DeleteGroundType(DeleteView):
    template_name = 'confirm_delete.html'
    model = GroundType
    success_url = reverse_lazy('insert_data')

class InsertGroundType(CreateView):
    template_name = "form.html"
    form_class = GroundTypeModelForm
    success_url = reverse_lazy('insert_data')

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



class AuctionTemplateView(TemplateView):
    template_name = "auction.html"

    def post(self, request, pk):
        context_ = self.get_context_data()
        bid_ = Bid.objects.create( auction = context_['auction'],
                            user = Profile.objects.get(user=request.user),
                            bid_amount = request.POST.get('bid_amount'),
                                )

        return render(request, 'auction.html', context_ )

    def get_context_data(self, **kwargs):
        context_= super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        auction_ = Auction.objects.get(id=pk)
        context_['auction'] = auction_
        context_['form'] = BidModelForm
        if Bid.objects.filter(auction_id=pk).exists():
            context_['last_one'] = Bid.objects.filter(auction_id=pk).latest("created")
        else:
            pass
        return context_



class AuctionsTemplateView(TemplateView):
    template_name = "auctions.html"
    extra_context = {'auctions': Auction.objects.all()}



class ImageCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('home')
    permission_required = 'viewer.add_image'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class ImageUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('images')
    model = Image
    permission_required = 'viewer.change_image'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a creator.')
        return super().form_invalid(form)


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Image
    success_url = reverse_lazy('images')
    permission_required = 'viewer.delete_image'


class ImageDetailView(DetailView):
    model = Image
    template_name = 'image.html'


def cities(request):
        cities_ = Cities.objects.all()
        context = {'cities': cities_}
        return render(request, 'cities.html', context)

class Insertcity(CreateView):
    template_name = "form.html"
    form_class = CitiesModelForm
    success_url = reverse_lazy('insert_data')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class DeleteCity(DeleteView):
    template_name = 'confirm_delete.html'
    model = Cities
    success_url = reverse_lazy('insert_data')


class InsertHouseType(CreateView):
    template_name = "form.html"
    form_class = HouseTypeModelForm
    success_url = reverse_lazy('insert_data')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class InsertAparmentType(CreateView):
    template_name = "form.html"
    form_class = ApartmentTypeModelForm
    success_url = reverse_lazy('insert_data')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

def bid(request, pk):
    if Bid.objects.filter(id=pk).exists():
        bid_ = Bid.objects.get(id=pk)
        context = {'bid': bid_}
        return render(request, 'auction.html', context)
    return grounds(request)