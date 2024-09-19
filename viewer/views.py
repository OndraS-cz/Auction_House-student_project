from django.shortcuts import render

# Create your views here.
def ten_cas(request):
    return render(request, 'ten_cas.html')