from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, JsonResponse
# Create your views here.


def cart(requset_parham):
    from .models import Cart
    from products.models import Products
    id_usere_taraf = requset_parham.user
    carts = Cart.objects.filter(id_user=id_usere_taraf)
    geymatehame = 0
    mojodiat = len(carts)
    for i in carts:
        z = i.id_product.id
        geymat = (Products.objects.get(id=z)).price
        i.product_price = geymat
        geymate_nahay = i.count * geymat
        i.total_price = geymate_nahay
        geymatehame += i.total_price
    return render(requset_parham, 'cart/cart.html', {'m': carts,'gh': geymatehame, 'vojod': mojodiat})


def cart_plus(request_parham):

    from .models import Products
    from cart.models import Cart
    from django.contrib.auth.models import User
    if request_parham.method == 'POST':
        user_id = request_parham.POST.get("user_id", 0)
        user = User.objects.get(id=user_id)
        id_pro = request_parham.POST.get('id_pro', 0)
        id_pro = int(id_pro)
        pro_dict = {}
        try:
            p = Products.objects.get(id=id_pro)
        except Products.DoesNotExist:
            return HttpResponse('mahsool vojood nadarad')
        sabad = Cart.objects.get(id_product=p, id_user=user.id)
        pc_count = sabad.count + 1
        if p.count - pc_count >= 0:
            sabad.count += 1
            sabad.product_price = p.price
            sabad.total_price += sabad.product_price
            sabad.save()
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        else:
            return HttpResponse('too bagesh dare ! ! !')

    else:
        return HttpResponse('darkhast post nist?')

def cart_minus(request_parham):
    from .models import Products
    from cart.models import Cart
    from django.contrib.auth.models import User
    if request_parham.method == 'POST':
        user_id = request_parham.POST.get("user_id2", 0)
        user = User.objects.get(id=user_id)
        id_pro = request_parham.POST.get('id_pro2', 0)
        id_pro = int(id_pro)
        pro_dict = {}
        try:
            p = Products.objects.get(id=id_pro)
        except Products.DoesNotExist:
            return HttpResponse('mahsool vojood nadarad')
        sabad = Cart.objects.get(id_product=p, id_user=user.id)
        pc_count = sabad.count + 1
        if sabad.count > 1:
            sabad.count -= 1
            sabad.product_price = p.price
            sabad.total_price = sabad.product_price * sabad.count
            sabad.save()
            return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
        if sabad.count == 1:
            sabad.delete()

            return HttpResponse('mojoodie sabad tamoom shod')

    else:
        return HttpResponse('darkhast post nist?')


def cart_pak(request_parham):
    print('inja ! ! ! ')
    from .models import Cart
    from django.contrib.auth.models import User
    if request_parham.method == 'POST':
        carto = request_parham.POST.get('id_cart', 0)
        usero = request_parham.POST.get('user_id2', 0)
        usero2 = User.objects.get(id=usero)
        carto = int(carto)
        z = Cart.objects.get(id=carto, id_user=usero2.id)
        z.delete()
        return HttpResponse('pak shod')
    else:
        return Http404
# def cart_pak(request_parham):
#     pro_dict = {}
#     if request_parham.method == "POST":
#         id_cart = request_parham.POST.get("id_cart", 0)
#         user_id = request_parham.POST.get("user_id", 0)
#         try:
#             id_cart = int(id_cart)
#         except (ValueError, TypeError, SyntaxError):
#             return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
#         if not id_cart or id_cart <= 0:
#             return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
#         if user_id:
#             from django.contrib.auth.models import User
#             try:
#                 user = User.objects.get(id=user_id)
#             except User.DoesNotExist:
#                 print("User.DoesNotExist")
#                 return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
#         else:
#             print("user_id bug")
#             return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
#         from .models import Cart
#         cart = Cart.objects.get(id_user=user, id=id_cart)
#         if cart.count > 0:
#             cart.delete()
#             pro_dict = Cart.objects.filter(id_user=user)
#         elif cart.count <= 0:
#             return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=False)
#     return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=False)