from django.db.models.functions import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q, Subquery, OuterRef
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, TemplateView, ListView, CreateView, DetailView
from django.views import View

from accounts.models import Profile

from viewer.forms import CitiesModelForm, HouseTypeModelForm, ApartmentTypeModelForm, GroundTypeModelForm, BidModelForm, \
    ImageModelForm, AuctionModelForm, PropertyTypeModelForm, \
    PropertyTypeForm, HouseForm, ApartmentForm, GroundForm
from viewer.models import House, Apartment, Ground, Auction, Image, Bid, HouseType, ApartmentType, Cities, GroundType, \
    PropertyType

from logging import getLogger

LOGGER = getLogger()


def home(request):
    auctions = Auction.objects.order_by('?')[:5]
    context = {
        'auctions': auctions
    }
    return render(request, "home.html", context)


def select_property_type(request):
    if request.method == 'POST':
        form = PropertyTypeForm(request.POST)
        if form.is_valid():
            property_type = form.cleaned_data['property_type']

            if property_type == 'house':
                return redirect('create_house')
            elif property_type == 'apartment':
                return redirect('create_apartment')
            elif property_type == 'ground':
                return redirect('create_ground')
    else:
        form = PropertyTypeForm()

    return render(request, 'form_select.html', {'form': form})


def create_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insert_property_type')
    else:
        form = HouseForm()

    return render(request, 'form_create.html', {'form': form})


def create_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insert_property_type')
    else:
        form = ApartmentForm()

    return render(request, 'form_create.html', {'form': form})


def create_ground(request):
    if request.method == 'POST':
        form = GroundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insert_property_type')
    else:
        form = GroundForm()

    return render(request, 'form_create.html', {'form': form})


def create_auction(request):
    if request.method == 'POST':
        form = AuctionModelForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit=False)

            auction.estimate_value = form.cleaned_data['estimate_value']
            auction.min_value = form.cleaned_data['min_value']
            auction.auction_assurance = form.cleaned_data['auction_assurance']
            auction.min_bid = form.cleaned_data['min_bid']
            auction.date_auction = form.cleaned_data['date_auction']
            auction.date_end_auction = form.cleaned_data['date_end_auction']
            auction.auction_description = form.cleaned_data['auction_description']
            auction.preview_image = form.cleaned_data['preview_image']

            auction.save()

            return redirect('insert_data')
    else:
        form = AuctionModelForm()

    return render(request, 'form_create.html', {'form': form})


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
    permission_required = 'viewer.delete_housetype'


class HousesListView(ListView):
    template_name = "houses.html"
    model = House
    context_object_name = 'houses'


def auction_houses(request):
    current_date = datetime.datetime.now()
    auction_houses = Auction.objects.filter(property_type__house__isnull=False).order_by('date_auction')
    future_auctions = Auction.objects.filter(property_type__house__isnull=False, date_auction__gte=current_date).order_by('date_auction')
    past_auctions = Auction.objects.filter(property_type__house__isnull=False, date_end_auction__lt=current_date).order_by('date_auction')
    ongoing_auctions = Auction.objects.filter(property_type__house__isnull=False, date_end_auction__gte=current_date,
                                              date_auction__lte=current_date).order_by('date_auction')
    return render(request, 'auction_houses.html',
                  {'auction_houses': auction_houses,
                   'future_auctions': future_auctions,
                   'past_auctions': past_auctions,
                   'ongoing_auctions': ongoing_auctions})


class InsertDataListView(ListView):
    template_name = "insert_data.html"
    model = Auction
    context_object_name = 'insert_data'


class InsertHouse(PermissionRequiredMixin, CreateView):
    template_name = 'form_create.html'
    form_class = HouseForm
    success_url = reverse_lazy('insert_property_type')
    permission_required = 'viewer.add_house'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class UpdateHouse(PermissionRequiredMixin, UpdateView):
    template_name = 'form_create_back.html'
    form_class = HouseForm
    success_url = reverse_lazy('insert_data')
    model = House
    permission_required = 'viewer.change_house'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class DeleteHouse(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = House
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_house'


class InsertApartments(PermissionRequiredMixin, CreateView):
    template_name = "form_create.html"
    form_class = ApartmentForm
    success_url = reverse_lazy('insert_property_type')
    permission_required = 'viewer.add_apartment'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class UpdateApartments(PermissionRequiredMixin, UpdateView):
    template_name = 'form_create_back.html'
    form_class = ApartmentForm
    success_url = reverse_lazy('insert_data')
    model = Apartment
    permission_required = 'viewer.change_apartment'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class DeleteApartments(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Apartment
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_apartment'


class InsertGrounds(PermissionRequiredMixin, CreateView):
    template_name = "form_create.html"
    form_class = GroundForm
    success_url = reverse_lazy('insert_property_type')
    permission_required = 'viewer.add_ground'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class UpdateGrounds(PermissionRequiredMixin, UpdateView):
    template_name = 'form_create_back.html'
    form_class = GroundForm
    success_url = reverse_lazy('insert_data')
    model = Ground
    permission_required = 'viewer.change_ground'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class DeleteGrounds(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Ground
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_ground'


class InsertPropertyType(PermissionRequiredMixin, CreateView):
    template_name = "form_create.html"
    form_class = PropertyTypeModelForm
    success_url = reverse_lazy('insert_auction')
    permission_required = 'viewer.add_propertytype'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class InsertAuction(PermissionRequiredMixin, CreateView):
    template_name = "form_create.html"
    form_class = AuctionModelForm
    success_url = reverse_lazy('image_create')
    permission_required = 'viewer.add_auction'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class UpdateAuction(PermissionRequiredMixin, UpdateView):
    template_name = 'form_create_back.html'
    form_class = AuctionModelForm
    success_url = reverse_lazy('insert_data')
    model = Auction
    permission_required = 'viewer.change_auction'

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
    current_date = datetime.datetime.now()
    auction_apartments = Auction.objects.filter(property_type__apartment__isnull=False).order_by('date_auction')
    future_auctions = Auction.objects.filter(property_type__apartment__isnull=False, date_auction__gte=current_date).order_by('date_auction')
    past_auctions = Auction.objects.filter(property_type__apartment__isnull=False, date_end_auction__lt=current_date).order_by('date_auction')
    ongoing_auctions = Auction.objects.filter(property_type__apartment__isnull=False, date_end_auction__gte=current_date,
                                              date_auction__lte=current_date).order_by('date_auction')
    return render(request, 'auction_apartments.html',
                  {'auction_apartments': auction_apartments,
                   'future_auctions': future_auctions,
                   'past_auctions': past_auctions,
                   'ongoing_auctions': ongoing_auctions})


class DeleteApartmentType(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = ApartmentType
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.delete_apartmenttype'


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
    permission_required = 'viewer.delete_groundtype'


class InsertGroundType(PermissionRequiredMixin, CreateView):
    template_name = "form_create.html"
    form_class = GroundTypeModelForm
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.add_groundtype'


class GroundsView(View):
    def get(self, request):
        grounds_ = Ground.objects.all()
        context = {'grounds': grounds_}
        return render(request, "grounds.html", context)


def auction_grounds(request):
    current_date = datetime.datetime.now()
    auction_grounds = Auction.objects.filter(property_type__ground__isnull=False).order_by('date_auction')
    future_auctions = Auction.objects.filter(property_type__ground__isnull=False,date_auction__gte=current_date).order_by('date_auction')
    past_auctions = Auction.objects.filter(property_type__ground__isnull=False, date_end_auction__lt=current_date).order_by('date_auction')
    ongoing_auctions = Auction.objects.filter(property_type__ground__isnull=False, date_end_auction__gte=current_date,
                                              date_auction__lte=current_date).order_by('date_auction')
    return render(request, 'auction_grounds.html',
                  {'auction_grounds': auction_grounds,
                   'future_auctions': future_auctions,
                   'past_auctions': past_auctions,
                   'ongoing_auctions': ongoing_auctions})


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
        if Profile.objects.filter(user=request.user).exists():
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
            context_['last_one'] = Bid.objects.filter(auction_id=pk).order_by('-created').first()
        else:
            context_['last_one'] = None
        return context_


class AuctionsTemplateView(ListView):
    template_name = "auctions.html"
    model = Auction
    context_object_name = 'auctions'


class InsertImage(PermissionRequiredMixin, CreateView):
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


def cities(request):
        cities_ = Cities.objects.all()
        context = {'cities': cities_}
        return render(request, 'cities.html', context)


class InsertCity(PermissionRequiredMixin, CreateView):
    template_name = "form_select.html"
    form_class = CitiesModelForm
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.add_cities'

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
    permission_required = 'viewer.delete_propertytype'


class InsertHouseType(PermissionRequiredMixin, CreateView):
    template_name = "form_select.html"
    form_class = HouseTypeModelForm
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.add_housetype'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


class InsertApartmentType(PermissionRequiredMixin, CreateView):
    template_name = "form_create.html"
    form_class = ApartmentTypeModelForm
    success_url = reverse_lazy('insert_data')
    permission_required = 'viewer.add_apartmenttype'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data updating.')
        return super().form_invalid(form)


def auction_bids(request, pk):
    bids = Bid.objects.filter(auction_id = pk)
    return render(request, 'auction_bids.html', {'bids': bids})


def won_auctions_view(request):
    try:
        last_bid = Bid.objects.filter(
            auction=OuterRef('pk')
        ).order_by('-created').values('user')[:1]
        won_auctions = Auction.objects.filter(
            date_end_auction__lt=datetime.datetime.now()
        ).annotate(
            last_bid_user=Subquery(last_bid)
        ).filter(
            last_bid_user=request.user.profile
        )
        context = {
            'won_auctions': won_auctions
        }
        return render(request, 'won_auctions.html', context)
    except Exception as e:
        return redirect('home')


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


def contact(request):
    return render(request, 'contact.html')
