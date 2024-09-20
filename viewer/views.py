from django.shortcuts import render

from viewer.models import *


# Create your views here.

def home(request):
    return render(request, 'home.html')
def detail(request, pk):
    if Property.objects.filter(id=pk).exists():
        property_ = Property.objects.get(id=pk)
        house_ = House.objects.get(id=pk)
        ground_ = Ground.objects.get(id=pk)
        apartment_ = Apartment.objects.get(id=pk)
        context = {'property': property_, 'cas': house_.name}
    return render(request, 'detail.html', context)