from django.contrib import admin
from .models import pprofile
# Register your models here.


# class ProductAdmin(admin.ModelAdmin):      #esmesh ekhtiarie
#     list_display = ['name', 'id', 'price', 'tozihat', 'count', 'deleted']
#
#
# admin.site.register(Products, ProductAdmin)        #too qrguman badish be class bala eshare mikonim
admin.site.register(pprofile)
