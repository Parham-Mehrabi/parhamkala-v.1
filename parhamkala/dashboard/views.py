from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
# Create your views here.


def home(request_parham):

    if request_parham.user and request_parham.user.is_authenticated:
        from cart.models import Cart

        return render(request_parham,"account/dashboard.html", {'par': 1})

#    else:

    return render(request_parham, "account/dashboard.html", {'par': 2})


def p_404(request_parham, exception):
    return render(request_parham, 'errors/404_2.html')