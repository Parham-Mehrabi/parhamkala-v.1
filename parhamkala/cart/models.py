from django.db import models
from products.models import Products
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    id_product = models.ForeignKey(Products, verbose_name="نام محصول", on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, verbose_name="نام کاربری", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1, blank=True, verbose_name="تعداد")
    total_price = models.PositiveIntegerField(verbose_name="مبلغ نهایی")
    product_price = models.PositiveIntegerField(verbose_name="مبلغ واحد", blank=True)
    def __str__(self):
        return self.id_user.username