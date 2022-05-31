from django.shortcuts import render, HttpResponse, Http404, redirect
from .models import Products, Categories, SubCategories
from django.http import HttpResponse, Http404, JsonResponse
# Create your views here.


def index2(request_parham):


    p1 = Categories.objects.all()
    p2 = SubCategories.objects.all()
    sub_cate = []
    for i2 in p2:
        sub_cate.append([i2.name, i2.parent.id, i2.id])

    p3 = Products.objects.filter(deleted=False)
    prod = []
    for i3 in p3:
        prod.append([i3.name, i3.category.id, i3.price, i3.count, i3.id])

    if request_parham.user and request_parham.user.is_authenticated:
        return render(request_parham, "product/product.html", {'categories': p1,
                                                               'subcategories': sub_cate,
                                                               'product': prod,
                                                               'par': 1}
                      )

    else:
        return render(request_parham, "product/product.html", {'categories': p1,
                                                               'subcategories': sub_cate,
                                                               'product': prod,
                                                               'par': 2}
                      )


def index(request_parham):


    p1 = Categories.objects.all()
    cate = []
    for i in p1:
        cate.append([i.name, i.id])

    p2 = SubCategories.objects.all()
    sub_cate = []
    for i2 in p2:
        sub_cate.append([i2.name, i2.parent.id, i2.id])

    p3 = Products.objects.filter(deleted=False)
    prod = []
    for i3 in p3:
        prod.append([i3.name, i3.category.id, i3.price, i3.count, i3.id])
    if request_parham.user.is_superuser:

        return render(request_parham, "product/product_admin.html", {'categories': cate,
                                                                     'subcategories': sub_cate,
                                                                     'product': prod}
                    )
    else:
        return Http404


def delete(request_parham, id_p=None):
    if not id_p:
        redirect("products")
    p = Products.objects.get(id=id_p)
    p.deleted = True
    p.save()
    print("delete", id_p)
#   return HttpResponse("delete products")
    return redirect("products")


def delete_pro(request_parham):
    if request_parham.method == "GET":
        command = request_parham.GET.get("command", None)
        id = request_parham.GET.get("id", None)
        print(command, id)
        try:
            if id:
                id = int(id)
            else:
                raise TypeError
        except:
            return HttpResponse("داداش داری اشتباه میزنی")
        if command == "delete":
            try:
                p = Products.objects.get(id=id)
                # p.delete()
                p.deleted = True
                p.save()
            except Products.DoesNotExist:
                return HttpResponse("محصولی وجود ندارد")
        else:
            return HttpResponse("دستور اشتباه است")

        return HttpResponse(command + " : " + str(id) + "پاک شد")
    else:
        return Http404


def edit(request_parham, id_pro=None):
    if request_parham.method == "GET":
        p = Products.objects.filter(id=id_pro, deleted=False)
        if len(p) == 1:
            list_of_product = []
            for i in p:
                list_of_product.append([i.name, i.count, i.price, i.category.name, i.id])
            return render(request_parham, "product/edit.html", {"list": list_of_product})

    elif request_parham.method == "POST":

        namejadid = request_parham.POST.get("name_mahsool", False)
        tedadejadid = request_parham.POST.get("tedad_mahsool", False)
        gheymatejadid = request_parham.POST.get("geymat_mahsool", False)
        subejadid = request_parham.POST.get("daste_mahsool", False)
        try:
            aa = SubCategories.objects.get(name=subejadid)
        except SubCategories.DoesNotExist:
            return HttpResponse("in sube jadid vojood nadare")

        p2 = Products.objects.get(id= id_pro)

        p2.category = aa
        p2.name = namejadid
        p2.count = tedadejadid
        p2.price = gheymatejadid
        p2.save()
        return redirect('products')


def add(request_parham):
    if request_parham.method == "POST":
        from .models import Products, Categories, SubCategories

        name_product = request_parham.POST.get("name_product", False)
        price_product = request_parham.POST.get("price_product", False)
        count_product = request_parham.POST.get("count_product", False)
        subcategory_product = request_parham.POST.get("subcategory_product", False)
        category_product = request_parham.POST.get("category_product", False)
        if False in [name_product, price_product, count_product, subcategory_product, category_product]:
            return HttpResponse("اطلاعات را به طور کامل وارد نمایید")
        else:
            try:
                s_c = SubCategories.objects.get(name=SubCategories)

                p = Products()
                p.name = name_product
                p.price = int(price_product)
                p.count = int(count_product)
                p.category = s_c
                p.save()
                return HttpResponse("محصول " + name_product + " با موفقیت اضافه شد")
            except SubCategories.DoesNotExist:
                # زمانی که در رکورد مورد نظر زیر دسته بندی موجود نباشه
                try:
                    c_p = Categories.objects.get(id=category_product)
                    # در اینجا پیشنهاد میشه که در جدول های دیتابیس زیردسته بندی آیدی رو از حالت دستی حذف کنید

                    sub = SubCategories()
                    sub.name = subcategory_product
                    sub.parent = c_p
                    sub.save()
                    # ساخت یک زیر دسته بندی جدید
                    s_c = SubCategories.objects.get(name=subcategory_product)
                    # ساخت یک محصول جدید
                    p = Products()
                    p.name = name_product
                    p.price = int(price_product)
                    p.count = int(count_product)
                    p.category = s_c
                    p.save()
                    return HttpResponse("محصول " + name_product + " با موفقیت اضافه شد")
                except Categories.DoesNotExist:
                    return HttpResponse(
                        "دسته بندی" + category_product + "وجود ندارد لطفا یک دسته بندی درست وارد نمایید")
    else:
        return Http404()


def add_cart(request_parham):
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
        try:
            sabad = Cart.objects.get(id_product=p, id_user=user.id)
            pc_count = sabad.count+1
            if p.count - pc_count >= 0:
                sabad.count += 1
                sabad.product_price = p.price
                sabad.total_price += sabad.product_price
                sabad.save()
                return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)
            else:
                return HttpResponse('too bagesh dare ! ! !')

        except Cart.DoesNotExist:
            newcart = Cart()
            if p.count > 0:
                newcart.id_product = p
                newcart.id_user = user
                newcart.product_price = p.price
                newcart.total_price = p.price
                newcart.save()
                print('agar biad inja chi3')
                return JsonResponse(pro_dict, json_dumps_params={'ensure_ascii': False}, safe=True)

            else:
                return HttpResponse('tamoom shode mahsool  ! ! !')

    else:
        return HttpResponse('darkhast post nist?')


def product_details(request_parham, id_pro=None):
    # todo
    # ino kamel konam
    return render(request_parham, 'product/product_details.html')


def product_dastebandi(request_parham, ism):
    from .models import SubCategories, Categories
    try:
        category = Categories.objects.get(name=ism)
        subcate = SubCategories.objects.filter(parent=category)
        products = []
        for p in subcate:
            pof = Products.objects.filter(category=p, deleted=False)
            for i3 in pof:
                products.append([i3.name, i3.category.id, i3.price, i3.count, i3.id])
        other_categories = Categories.objects.all()
        return render(request_parham, "product/product.html", {'product': products, 'categories': other_categories, 'oon':category })
    except Categories.DoesNotExist:
        return redirect('products')

