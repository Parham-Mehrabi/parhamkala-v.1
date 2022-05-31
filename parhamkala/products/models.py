from django.db import models

# Create your models here.


class Categories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name="نام دسته بندی")

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name="نام دسته بندی")
    parent = models.ForeignKey(Categories, verbose_name="دسته بندی", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Products(models.Model):
    # ProImage1 = models.ImageField(upload_to="shop")
    # ProImage2 = models.ImageField(upload_to="shop", blank=True, null=True)
    # ProImage3 = models.ImageField(upload_to="shop", blank=True, null=True)
    # ProImage4 = models.ImageField(upload_to="shop", blank=True, null=True)
    tozihat = models.CharField(max_length=500, verbose_name='توضیحات', blank=True)
    name = models.CharField(max_length=50, verbose_name="نام دسته بندی")
    category = models.ForeignKey(SubCategories, verbose_name="دسته بندی", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0, blank=True, verbose_name="تعداد محصول")
    price = models.PositiveIntegerField(verbose_name="قیمت محصول")
    deleted = models.BooleanField(verbose_name="محصول حذف شده", blank=True, default=False)

    def __str__(self):
        return self.name

 #    def get(self):
 #        return self.tozihat[0:    30]
 #