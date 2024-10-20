from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.core.exceptions import PermissionDenied
from django.utils.http import url_has_allowed_host_and_scheme

from accounts.forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


@login_required
def user_logout(request):
    referer = request.META.get('HTTP_REFERER')

    if referer and url_has_allowed_host_and_scheme(referer, allowed_hosts=request.get_host()):
        try:
            request.user.has_perm('app.view_protected_page')
            return_url = reverse('home')
        except PermissionDenied:
            return_url = referer
    else:
        return_url = reverse('home')

    logout(request)
    return redirect(return_url)
