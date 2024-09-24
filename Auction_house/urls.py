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
from django.contrib import admin
from django.urls import path

from viewer.views import home, GroundsListView, ground, HousesListView, house, \
    ApartmentsListView, apartment, AuctionsListView, auction, UpdateHouse, UpdateApartments, UpdateGrounds, \
    UpdateAuction, DeleteHouse, DeleteApartments, DeleteGrounds, DeleteAuction
from viewer.views import home, houses, apartments, insert_data, InsertHouse, InsertApartments, InsertGrounds, \
    InsertAuction, InsertPropertytype

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('houses/', HousesListView.as_view(), name='houses'),
    path('house/<pk>/', house, name='house'),

    path('apartments/', ApartmentsListView.as_view(), name='apartments'),
    path('apartment/<pk>/', apartment, name='apartment'),

    path('grounds/', GroundsListView.as_view(), name='grounds'),
    path('ground/<pk>/', ground, name='ground'),

    path('auctions/', AuctionsListView.as_view(), name='auctions'),
    path('auction/<pk>/', auction, name='auction'),


    path('insert/', insert_data, name="insert_data"),


    path('insert/houses', InsertHouse.as_view(), name="insert_houses"),
    path('update/houses/<pk>', UpdateHouse.as_view(), name="update_houses"),
    path('delete/houses/<pk>', DeleteHouse.as_view(), name="delete_houses"),


    path('insert/apartments', InsertApartments.as_view(), name="insert_apartments"),
    path('update/apartments/<pk>', UpdateApartments.as_view(), name="update_apartments"),
    path('delete/apartments/<pk>', DeleteApartments.as_view(), name="delete_apartments"),


    path('insert/grounds', InsertGrounds.as_view(), name="insert_grounds"),
    path('update/grounds/<pk>', UpdateGrounds.as_view(), name="update_grounds"),
    path('delete/grounds/<pk>', DeleteGrounds.as_view(), name="delete_grounds"),


    path('insert/property_type', InsertPropertytype.as_view(), name="insert_property_type"),


    path('insert/auction', InsertAuction.as_view(), name='insert_auction'),
    path('upadte/auction/<pk>', UpdateAuction.as_view(), name='update_auction'),
    path('delete/auction/<pk>', DeleteAuction.as_view(), name="delete_auction"),
]
