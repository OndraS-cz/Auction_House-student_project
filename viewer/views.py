from django.shortcuts import render

from viewer.models import Property


# Create your views here.
def detail(request, pk):
    context = {'cas': Property.loc_time()}
    return render(request, 'detail.html', context)