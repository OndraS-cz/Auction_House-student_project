from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Model, ImageField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from viewer.forms import ImageModelForm
from viewer.models import House, Apartment, Ground, Auction, Image
#from viewer.forms import ImageModelForm

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


class ImageCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('home')
    permission_required = 'viewer.add_image'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class ImageDetailView(DetailView):
    model = Image
    template_name = 'image.html'