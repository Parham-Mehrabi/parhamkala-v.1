from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
factor_state = {
    (1, "پرداخت نشده"),
    (2, "در انتظار پرداخت"),
    (3, "پرداخت شده")
}

class Factors(models.Model):
    id_user = models.ForeignKey(User, verbose_name="نام کاربری", on_delete=models.CASCADE)
    pay_date = models.DateTimeField(default=datetime.now(), blank=True, verbose_name="تاریخ پرداخت")
    state = models.SmallIntegerField(choices=factor_state, default=1, blank=True, verbose_name="وضعیت پرداخت")
    create_date = models.DateTimeField(default=datetime.now(), blank=True, verbose_name="تاریخ ایجاد")
    total_price = models.PositiveIntegerField(verbose_name="مبلغ نهایی")


class FactorProducts(models.Model):
    id_factor = models.ForeignKey(Factors, verbose_name="فاکتور", on_delete= models.CASCADE)
    id_product = models.ForeignKey(Products, verbose_name="نام محصول", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1, blank=True, verbose_name="تعداد")
    total_price = models.PositiveIntegerField(verbose_name="مبلغ نهایی")