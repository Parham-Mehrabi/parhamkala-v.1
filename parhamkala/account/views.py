from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
# Create your views here.


def index(request_parham):
    return render(request_parham, "account/test.html")


def _login(request_parham):
    if request_parham.method == "POST":
        from django.contrib.auth import authenticate, login
        usernamep1 = request_parham.POST.get("username", None)
        passwordp1 = request_parham.POST.get("passw", None)

        user = authenticate(request_parham, username=usernamep1, password=passwordp1)  # azoon 2ta inja estefade mishe
        if user is not None:
            login(request_parham, user)
            return redirect("dashboard_home")
        else:
            return render(request_parham, "account/login.html", {"error": "user ia password eshtebah ast ! ! !"})
    elif request_parham.method == "GET":
        return render(request_parham, "account/login.html")
    else:
        return Http404()


def _logout(request_parham):
    from django.contrib.auth import logout
    if request_parham.user.is_authenticated:
        logout(request_parham)
    return redirect("dashboard_home")


def register(request_parham):
    if request_parham.method == "POST":
        from django.contrib.auth.models import User

        username = request_parham.POST.get('username', None)
        fullname = request_parham.POST.get('fname', None)
        if isinstance(fullname, str) and fullname.index(" ") > 0:
            first_name, lastname = fullname.split()
        else:
            first_name = lastname = ""
        password = request_parham.POST.get("passwd", None)
        email = request_parham.POST.get('email', None)
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = lastname
        user.save()
        return redirect("login")
    elif request_parham.method == "GET":
        if request_parham.user and request_parham.user.is_authenticated:
            return redirect('dashboard_home')
    return render(request_parham, 'account/register.html')


def register2(request_parham):
    from .forms import registerform
    if request_parham.method == 'POST':
        form = registerform(request_parham.POST or None)
        if form.is_valid():
            from django.contrib.auth.models import User
            first_name = form.cleaned_data["fname"]
            lastname = form.cleaned_data["last_name"]
            username = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data["passw"]
            # password = form.cleaned_data.get("passw")
            # mishe get bezani tuple begiri ia nazani list begiri
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = lastname
            user.save()
            return redirect('login')
        return render(request_parham, 'account/register2.html',{'form':form})
    elif request_parham.method == 'GET':
        form = registerform()
        return render(request_parham, 'account/register2.html', {'form': form})
    else:
        return HttpResponse('oomad inja')







