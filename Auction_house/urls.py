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
from django.urls import path

from Auction_house import settings
from viewer.views import home, GroundsListView, ground, HousesListView, house, \
    ApartmentsListView, apartment, AuctionsListView, auction

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

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
