from django.contrib.auth.decorators import user_passes_test
from django.utils.timezone import now
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Max, F, Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, TemplateView, ListView, CreateView, DetailView
from django.views import View

from accounts.models import Profile

from viewer.forms import CitiesModelForm, HouseTypeModelForm, ApartmentTypeModelForm, GroundTypeModelForm, BidModelForm, ImageModelForm, ApartmentModelForm, GroundModelForm, HouseModelForm, AuctionModelForm, PropertyTypeModelForm
from viewer.models import House, Apartment, Ground, Auction, Image, Bid, HouseType, ApartmentType, Cities, GroundType, \
    PropertyType

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


class DeleteHouseType(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = HouseType
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_house_type'


class HousesListView(ListView):
    template_name = "houses.html"
    model = House
    context_object_name = 'houses'

def auction_houses(request):
    auction_houses = Auction.objects.filter(property_type__house__isnull=False)
    return render(request, 'auction_houses.html', {'auction_houses': auction_houses})

class InsertDataListView(PermissionRequiredMixin, ListView):
    template_name = "insert_data.html"
    model = Auction
    context_object_name = 'insert_data'
    permission_required = 'viewer.insert_data'


class InsertHouse(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = HouseModelForm
    success_url = reverse_lazy('insert_property_type')
    permission_required = 'viewer.insert_house'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class UpdateHouse(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = HouseModelForm
    success_url = reverse_lazy('insert_data')
    model = House
    permission_required = 'viewer.update_house'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class DeleteHouse(PermissionRequiredMixin, DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = House
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_house'


class InsertApartments(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = ApartmentModelForm
    success_url = reverse_lazy('insert_property_type')
    permission_required = 'viewer.insert_apartment'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class UpdateApartments(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = ApartmentModelForm
    success_url = reverse_lazy('insert_data')
    model = Apartment
    permission_required = 'viewer.update_apartment'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class DeleteApartments(PermissionRequiredMixin, DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = Apartment
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_apartment'


class InsertGrounds(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = GroundModelForm
    success_url = reverse_lazy('insert_property_type')
    permission_required = 'viewer.insert_ground'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class UpdateGrounds(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = GroundModelForm
    success_url = reverse_lazy('insert_data')
    model = Ground
    permission_required = 'viewer.update_ground'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class DeleteGrounds(PermissionRequiredMixin, DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = Ground
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_ground'


class InsertPropertyType(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = PropertyTypeModelForm
    success_url = reverse_lazy('insert_auction')
    permission_required = 'viewer.insert_property_type'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class InsertAuction(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = AuctionModelForm
    success_url = reverse_lazy('image_create')
    permission_required = 'viewer.insert_auction'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class UpdateAuction(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = AuctionModelForm
    success_url = reverse_lazy('insert_data')
    model = Auction
    permission_required = 'viewer.update_auction'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class DeleteAuction(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Auction
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_auction'


class InsertBid(CreateView):
    model = Bid
    template_name = "auction.html"
    form_class = BidModelForm
    success_url = reverse_lazy('auction')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
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


def apartment_types(request):
    apartment_types_ = ApartmentType.objects.all()
    context = {'apartment_types': apartment_types_}
    return render(request, 'apartment_types.html', context)


class ApartmentsView(View):
    def get(self, request):
        apartments_ = Apartment.objects.all()
        context = {'apartments': apartments_}
        return render(request, "apartments.html", context)

def auction_apartments(request):
    auction_aparmtnets = Auction.objects.filter(property_type__apartment__isnull=False)
    return render(request, 'auction_apartments.html', {'auction_apartments': auction_aparmtnets})


class DeleteApartmentType(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = ApartmentType
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_apartment_type'


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


class DeleteGroundType(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = GroundType
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_ground_type'


class InsertGroundType(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = GroundTypeModelForm
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.insert_ground_type'


class GroundsView(View):
    def get(self, request):
        grounds_ = Ground.objects.all()
        context = {'grounds': grounds_}
        return render(request, "grounds.html", context)

def auction_grounds(request):
    auction_grounds = Auction.objects.filter(property_type__ground__isnull=False)
    return render(request, 'auction_grounds.html', {'auction_grounds': auction_grounds})


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
        last_one = Bid.objects.filter(auction_id = pk).order_by("created").last()
        context_ = self.get_context_data()
        context_['last_one'] = last_one
        Bid.objects.create(auction = context_['auction'],
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
            context_['last_one'] = None
        return context_


class AuctionsTemplateView(ListView):
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


class InsertCity(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = CitiesModelForm
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.insert_cities'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class DeleteCity(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Cities
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_cities'


class PropertyTypesListView(ListView):
    template_name = "property_types.html"
    model = PropertyType
    context_object_name = 'property_types'

class DeletePropertyType(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = PropertyType
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_property_types'


class InsertHouseType(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = HouseTypeModelForm
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.insert_house_types'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class InsertApartmentType(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = ApartmentTypeModelForm
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.insert_apartment_type'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


def auction_bids(request, pk):
    bids = Bid.objects.filter(auction_id = pk)
    return render(request, 'auction_bids.html', {'bids': bids})


def won_auctions_view(request):
    won_auctions = Auction.objects.filter(
        date_end_auction__lt=now(),
        bid__user=request.user.profile
    ).annotate(
        highest_bid_amount=Max('bid__bid_amount')
    ).filter(
        bid__bid_amount=F('highest_bid_amount')
    )

    context = {
        'won_auctions': won_auctions
    }

    return render(request, 'win_auctions.html', context)


def auctions_list_view(request):
    query = request.GET.get('q')
    auctions = Auction.objects.all()

    if query:
        auctions = auctions.filter(
            Q(location__icontains=query) | Q(description__icontains=query)
        )

    context = {
        'auctions': auctions,
    }
    return render(request, 'auction_search.html', context)
