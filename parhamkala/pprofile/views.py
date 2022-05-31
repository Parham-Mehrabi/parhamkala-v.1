from django.shortcuts import render

# Create your views here.


def profile(request_parham):
    return render(request_parham, 'profile/profile.html')
