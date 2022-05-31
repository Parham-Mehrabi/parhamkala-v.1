from django.contrib.auth.models import User


def GlobalModels(request):
    from cart.models import Cart

    user = request.user
    c_count = 0
    if user and user.is_authenticated:
        lo = 1
        c = Cart.objects.filter(id_user=user)
        for i in c:
            c_count += i.count
    else:
        lo = 2
    return {"cart": c_count, "login": lo}
