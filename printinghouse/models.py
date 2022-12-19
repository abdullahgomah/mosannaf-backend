from django.db import models

from django_countries.fields import CountryField

# Create your models here.


class PrintingHouse(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=255)  # اسم
    # country = models.CharField(verbose_name="الدولة", max_length=150)  # دولة
    country = CountryField(verbose_name='دولة')
    territory = models.CharField(
        max_length=100, verbose_name='إقليم')  # اقليم
    county = models.CharField(
        max_length=100, verbose_name='مقاطعة')  # مقاطعة
    region = models.CharField(max_length=100, verbose_name='منطقة')  # منطقة
    city = models.CharField(max_length=100, verbose_name='مدينة')  # مدينة
    governorate = models.CharField(
        max_length=100, verbose_name='محافظة')  # محافظة
    village = models.CharField(max_length=100, verbose_name='قرية')  # قرية
    neighborhood = models.CharField(max_length=100, verbose_name='حي')  # حي
    street = models.CharField(max_length=100, verbose_name='شارع')  # شارع
    building = models.IntegerField(
        default=0, verbose_name='بناية رقم')  # بناية رقم
    floor = models.IntegerField(default=0, verbose_name='الدور')  # الدور
    unit = models.CharField(verbose_name='الوحدة', max_length=20)  # الوحدة
    nearest_landmark = models.CharField(
        max_length=150, verbose_name='أقرب معلم بارز')  # أقرب معلم بارز
    coordinates = models.CharField(
        max_length=100, verbose_name='إحداثيات')  # إحداثيات
    landline_number = models.CharField(
        max_length=20, verbose_name='هاتف رقم')  # هاتف رقم
    phone_number = models.CharField(
        max_length=20, verbose_name='جوال رقم')  # جوال رقم
    fax_number = models.CharField(
        max_length=25, verbose_name='فاكس رقم')  # فاكس رقم
    telex = models.CharField(max_length=50, verbose_name='تلكس')  # تلكس
    pobox = models.CharField(
        max_length=50, verbose_name='صندوق بريد')  # صندوق بريد
    postal_code = models.CharField(
        max_length=50, verbose_name='الرمز البريدي')  # الرمز البريدي
    email = models.EmailField(
        verbose_name="البريد الإلكتروني", max_length=150)  # البريد الإلكتروني


    # فنان الغلاف
    # سلسلة
    branch = models.ForeignKey(
        'Branch', verbose_name='القسم', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مطبعة'
        verbose_name_plural = "المطابع"


class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'قسم'
        verbose_name_plural = 'اﻷقسام'
