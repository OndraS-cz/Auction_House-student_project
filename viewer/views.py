from django.shortcuts import render

from viewer.models import House, Apartment


def home(request):
    return render(request, "home.html")

def houses(request):
    houses_ = House.objects.all()
    context = {'houses': houses_}
    return render(request, 'houses.html', context)


def apartments(request):
    apartments_ = Apartment.objects.all()
    context = {'apartments': apartments_}
    return render(request, 'apartments.html', context)
