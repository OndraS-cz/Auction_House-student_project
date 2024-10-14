"""
URL configuration for Auction_house project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Auction_house import settings

from accounts.views import SignUpView, user_logout

from viewer.views import home, InsertHouse, ApartmentsListView, apartment, ImageCreateView, \
    ImageDetailView, InsertApartments, InsertGrounds, InsertAuction, HousesListView, house, \
    GroundsListView, ground, UpdateHouse, DeleteHouse, UpdateApartments, DeleteApartments, UpdateGrounds, DeleteGrounds, \
    UpdateAuction, DeleteAuction, ImageUpdateView, ImageDeleteView, InsertPropertyType, AuctionTemplateView, \
    InsertCity, InsertHouseType, HouseTypesListView, DeleteHouseType, apartment_types, InsertApartmentType, \
    DeleteApartmentType, cities, DeleteCity, InsertGroundType, ground_types, DeleteGroundType, InsertBid, \
    InsertDataListView, AuctionsTemplateView, auction_bids, won_auctions_view, auctions_list_view, auction_houses, \
    auction_apartments, auction_grounds, PropertyTypesListView, DeletePropertyType

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('image/create', ImageCreateView.as_view(), name='image_create'),

    path('insert/bid', InsertBid.as_view(), name='insert_bid'),

    path('insert/', InsertDataListView.as_view(), name="insert_data"),

    path('insert/houses', InsertHouse.as_view(), name="insert_houses"),
    path('update/houses/<pk>', UpdateHouse.as_view(), name="update_houses"),
    path('delete/houses/<pk>', DeleteHouse.as_view(), name="delete_houses"),

    path('houses/', HousesListView.as_view(), name='houses'),
    path('house/<pk>/', house, name='house'),

    path('house_types/', HouseTypesListView.as_view(), name="house_types"),
    path('insert/house_types', InsertHouseType.as_view(), name="insert_house_type"),
    path('delete/house_type/<pk>', DeleteHouseType.as_view(), name="delete_house_type"),

    path('insert/apartments', InsertApartments.as_view(), name="insert_apartments"),
    path('update/apartments/<pk>', UpdateApartments.as_view(), name="update_apartments"),
    path('delete/apartments/<pk>', DeleteApartments.as_view(), name="delete_apartments"),

    path('apartments/', ApartmentsListView.as_view(), name='apartments'),
    path('apartment/<pk>/', apartment, name='apartment'),

    path('aparment_types/', apartment_types, name="apartment_types"),
    path('insert/apartment_types', InsertApartmentType.as_view(), name="insert_apartment_types"),
    path('delete/apartment_types/<pk>', DeleteApartmentType.as_view(), name="delete_apartment_types"),

    path('insert/grounds', InsertGrounds.as_view(), name="insert_grounds"),
    path('update/grounds/<pk>', UpdateGrounds.as_view(), name="update_grounds"),
    path('delete/grounds/<pk>', DeleteGrounds.as_view(), name="delete_grounds"),

    path('grounds/', GroundsListView.as_view(), name='grounds'),
    path('ground/<pk>/', ground, name='ground'),

    path('insert/ground_type', InsertGroundType.as_view(), name="insert_ground_type"),
    path('ground_types/', ground_types, name= 'ground_types'),
    path('delete/ground_type/<pk>', DeleteGroundType.as_view(), name="delete_ground_type"),

    path('insert/property_type', InsertPropertyType.as_view(), name="insert_property_type"),
    path('delete/property_type/<pk>', DeletePropertyType.as_view(), name="delete_property_type"),
    path('property_types', PropertyTypesListView.as_view(), name="property_types"),

    path('delete/cities/<pk>', DeleteCity.as_view(), name="delete_cities"),
    path('insert/cities', InsertCity.as_view(), name="insert_cities"),
    path('cities/', cities, name='cities'),

    path('insert/auction', InsertAuction.as_view(), name='insert_auction'),
    path('update/auction/<pk>', UpdateAuction.as_view(), name='update_auction'),
    path('delete/auction/<pk>', DeleteAuction.as_view(), name="delete_auction"),
    path('auctions/', AuctionsTemplateView.as_view(), name='auctions'),
    path('auctions_search/', auctions_list_view, name='auctions_list'),
    path('auction/<pk>/', AuctionTemplateView.as_view(), name='auction'),
    path('auction_bids/<pk>', auction_bids, name='auction_bids'),
    path('won_auctions', won_auctions_view ,name='won_auctions'),

    path('images/', ImageDetailView.as_view(), name='images'),
    path('image/create/', ImageCreateView.as_view(), name='image_create'),
    path('image/update/<pk>/', ImageUpdateView.as_view(), name='image_update'),
    path('image/delete/<pk>/', ImageDeleteView.as_view(), name='image_delete'),
    path('image/<pk>/', ImageDetailView.as_view(), name='image'),

    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/logout/', user_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('auctions/houses/', auction_houses, name='auction_houses'),
    path('auctions/apartments/', auction_apartments,  name='auction_apartments'),
    path('auctions/grounds/', auction_grounds, name='auction_grounds'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

