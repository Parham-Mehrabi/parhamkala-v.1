from django.db import models

# Create your models here.


class pprofile(models.Model):
    MY_CHOICES = (
        ('1', 'تهران'),
        ('2', 'خوزستان'),
        ('3', 'بوشهر'),
        ('4', 'خراسان رضوی'),
        ('5', 'اصفهان'),
        ('6', 'فارس'),
        ('7', 'آذربایجان شرقی'),
        ('8', 'مازندران'),
        ('9', 'کرمان'),
        ('10', 'البرز'),
        ('11', 'گیلان'),
        ('12', 'کهگیلویه و بویراحمد'),
        ('13', 'آذربایجان غربی'),
        ('14', 'هرمزگان'),
        ('15', 'مرکزی'),
        ('16', 'یزد'),
    )
    ostan = models.CharField(max_length=2, choices=MY_CHOICES, verbose_name="استان", blank=True)
    shahr = models.CharField(max_length=30, verbose_name='شهر', blank=True)
    adressesh = models.TextField(max_length=300, blank=True, verbose_name='آدرس')
    shomare = models.TextField(max_length=300, blank=True, verbose_name='شماره')
