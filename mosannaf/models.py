from django.db import models

from publisher.models import Publisher
from printinghouse.models import PrintingHouse

# Create your models here


class Mosannaf(models.Model):
    name = models.CharField(max_length=255, verbose_name='اسم المصنف')
    m_type = models.ForeignKey(
        'Type', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نوع المصنف')
    category = models.ForeignKey(
        "Category", verbose_name="فئة المصنف", on_delete=models.SET_NULL, null=True, blank=True)
    meaning = models.TextField(verbose_name='تفسير اسم المصنف')
    original_lang = models.ForeignKey(
        "Lang", verbose_name="أصل لغة المصنف", on_delete=models.SET_NULL, null=True, blank=True)
    date_published = models.DateField(
        verbose_name='تاريخ النشر', null=True, blank=True)
    parts_count = models.IntegerField(default=0, verbose_name='الأجزاء')
    pages_count = models.IntegerField(default=0, verbose_name='الصفحات')
    units_count = models.IntegerField(default=0, verbose_name='اﻷبواب')
    chapters_count = models.IntegerField(default=0, verbose_name='الفصول')
    # subject = models.ForeignKey("Subject", verbose_name="الموضوع",
    #                             on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.CharField(verbose_name="الموضوع", blank=True, null=True, max_length=100)
    # unit = models.ForeignKey("Unit", verbose_name='باب',
    #                          on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.CharField(max_length=200, verbose_name='الباب')
    # branch = models.ForeignKey("Branch", verbose_name='القسم',
    #                            on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.CharField(max_length=200, verbose_name="القسم")
    # sub_branch = models.ForeignKey(
    #     "SubBranch", verbose_name='القسم الفرعي', on_delete=models.SET_NULL, blank=True, null=True)
    sub_brnach = models.CharField(max_length=200, verbose_name="القسم الفرعي")
    
    # chapter = models.ForeignKey(
    #     "Chapter", verbose_name="الفصل", on_delete=models.SET_NULL, blank=True, null=True)
    chapter = models.CharField(max_length=200, verbose_name="الفصل")
    # field = models.ForeignKey(
    #     'Field', verbose_name='المجال', on_delete=models.SET_NULL, blank=True, null=True)
    field = models.CharField(max_length=200, verbose_name="المجال")

    # activity = models.ForeignKey(
    #     "Activity", verbose_name='النشاط', on_delete=models.SET_NULL, blank=True, null=True)
    activity = models.CharField(max_length=200, verbose_name="النشاط")

    summary = models.TextField(verbose_name='نبذه عن المصنف')
    image = models.ImageField(verbose_name='صورة المصنف', upload_to='أغلفة/',
                              height_field=None, width_field=None, max_length=None)
    file = models.FileField(verbose_name='ملف المصنف',
                            upload_to='مصنفات/', max_length=100)
    m_format = models.ForeignKey(
        "Formats", verbose_name="صيغة المصنف", blank=True, null=True, on_delete=models.SET_NULL)

    # m_form = models.ForeignKey(
    #     "Forms", verbose_name="شكل المصنف", blank=True, null=True, on_delete=models.SET_NULL)
    m_form = models.CharField(max_length=200, verbose_name="شكل المصنف")

    # size = models.ForeignKey(
    #     "Size", verbose_name="حجم المصنف", blank=True, null=True, on_delete=models.SET_NULL)
    m_size = models.CharField(max_length=200, verbose_name="حجم المصنف")


    # measurement = models.ForeignKey(
    #     "Measurement", verbose_name="قياس المصنف", blank=True, null=True, on_delete=models.SET_NULL)

    measurement = models.CharField(max_length=200, verbose_name="قياس المصنف")


    # preparation = models.ForeignKey(
    #     "Preparation", verbose_name='إعداد', on_delete=models.SET_NULL, blank=True, null=True)
    preparation = models.CharField(max_length=200, verbose_name="إعداد")
    

    # author = models.ForeignKey(
    #     "Author", verbose_name='تأليف', on_delete=models.SET_NULL, blank=True, null=True)

    author = models.CharField(max_length=200, verbose_name="تأليف")


    # checker = models.ForeignKey(
    #     "Checker", verbose_name='المحقق', on_delete=models.SET_NULL, blank=True, null=True)
    checker = models.CharField(max_length=200, verbose_name="المحقق")
    

    publisher = models.ForeignKey(
        "publisher.Publisher", verbose_name='ناشر', on_delete=models.SET_NULL, blank=True, null=True)

    print_year = models.CharField(verbose_name="سنة الطباعة", max_length=20)
    print_number = models.CharField(verbose_name="رقم الطباعة", max_length=20)

    printing_house = models.ForeignKey(PrintingHouse, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المطبعة")

    publish_year = models.CharField(verbose_name="سنة النشر", max_length=20)
    # publish_year = models.DateField(verbose_name="سنة النشر", viewMode='years')

    isbn = models.CharField(verbose_name='ردمك', max_length=50)

    #18# ردمد 
    issn = models.CharField(verbose_name='ردمد', max_length=50)

    #19# رقم الايداع
    deposit_number = models.CharField(
        verbose_name='رقم الايداع', max_length=60)

    # iso 
    iso = models.CharField(max_length=200, verbose_name='ايزو')


    #20# فنان الغلاف 
    cover_artist = models.CharField(max_length=200, verbose_name="فنان الغلاف")
    


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مصنف'
        verbose_name_plural = 'المصنفات'


# تقييم المصنف
class Rate(models.Model):
    mosannaf = models.ForeignKey(Mosannaf, on_delete=models.CASCADE, verbose_name="المصنف", related_name='mosannaf_rate')
    details = models.CharField(max_length=250, verbose_name="التقييم")

    def __str__(self):
        return f"تقييم {self.mosannaf.name}"
    
    class Meta:
        verbose_name = 'تقييم'
        verbose_name_plural = "التقييمات"




class Type(models.Model):
    name = models.CharField(max_length=250, verbose_name='نوع المصنف')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نوع المصنف'
        verbose_name_plural = 'أنوع المصنفات'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='فئة المصنف')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فئة المصنف'
        verbose_name_plural = 'فئات المصنفات'


class Lang(models.Model):
    name = models.CharField(max_length=50, verbose_name='اللغة')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'لغة'
        verbose_name_plural = 'اللغات'


# جدول الباب
class Unit(models.Model):
    name = models.CharField(max_length=255, verbose_name='باب')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'باب'
        verbose_name_plural = 'الأبواب'


# جدول الموضوع
class Subject(models.Model):
    name = models.CharField(verbose_name='موضوع', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'المواضيع'


# جدول القسم
class Branch(models.Model):
    name = models.CharField(max_length=200, verbose_name="القسم")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'قسم'
        verbose_name_plural = 'اﻷقسام'


# جدول القسم الفرعي
class SubBranch(models.Model):
    branch = models.ForeignKey(
        "Branch", verbose_name='القسم', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name="القسم الفرعي")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "قسم الفرعي"
        verbose_name_plural = "اﻷقسام الفرعية"

# جدول المجال


class Field(models.Model):
    name = models.CharField(max_length=250, verbose_name='اسم المجال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مجال'
        verbose_name_plural = 'المجالات'

# جدول النشاط


class Activity(models.Model):
    name = models.CharField(max_length=250, verbose_name='اسم النشاط')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نشاط'
        verbose_name_plural = 'الأنشطة'


# صيغ المصنفات
class Formats(models.Model):
    name = models.CharField(max_length=20, verbose_name='اسم الصيغة')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'صيغة مصنف'
        verbose_name_plural = 'صيغ المصنفات'


# جدول شكل المصنف
class Forms(models.Model):
    name = models.CharField(max_length=50, verbose_name='الشكل')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شكل مصنف'
        verbose_name_plural = 'أشكال المصنفات'


class Size(models.Model):
    name = models.CharField(max_length=50, verbose_name='الحجم')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'حجم مصنف'
        verbose_name_plural = 'أحجام المصنفات'


class Measurement(models.Model):
    name = models.CharField(max_length=50, verbose_name='القياس')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'قياس مصنف'
        verbose_name_plural = 'قياسات المصنفات'


# preparation
class Preparation(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'معد'
        verbose_name_plural = 'المعدين'


# authors
class Author(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مؤلف'
        verbose_name_plural = 'المؤلفون'


# checkers
class Checker(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'محقق'
        verbose_name_plural = 'المحققين'


class Chapter(models.Model):
    name = models.CharField(max_length=150, blank=True,
                            null=True, verbose_name='الاسم')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فصل'
        verbose_name_plural = 'الفصول'



## Translated Mosannaf مصنف مترجم
class TranslatedMosannaf(models.Model):
    mosannaf = models.ForeignKey(Mosannaf, on_delete=models.CASCADE, verbose_name='المصنف')

    #1# اللغة 
    language = models.ForeignKey(Lang, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='اللغة')

    #2# تاريخ الإصدار المترجم
    data_published = models.DateField(auto_now=False, verbose_name="تاريخ الإصدار المترجم", null=True, blank=True)

    #3# ناشر الترجمة
    translate_publisher = models.CharField(max_length=200, verbose_name='ناشر الترجمة')

    #4# صورة المصنف المترجم
    cover = models.ImageField(verbose_name="صورة المصنف المترجم", upload_to="Motargam/Covers")

    #5# صيغة المصنف 
    tm_format = models.ForeignKey(Formats, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="صيغة المترجم")

    #6# شكل المصنف 
    tm_form = models.CharField(max_length=200, null=True, blank=True, verbose_name="شكل المصنف")

    #7# حجم المصنف
    tm_size = models.CharField(max_length=100, verbose_name='حجم المصنف المترجم') 

    #8# قياس المصنف
    tm_mesaurement = models.CharField(max_length=100, verbose_name="قياس المصنف")

    #9# إعداد 
    preparation = models.CharField(max_length=100, verbose_name='اعداد')

    #10 حقل المؤلف
    publisher = models.CharField(max_length=100, verbose_name="الناشر")
    
    #11# المحقق 
    checker = models.CharField(max_length=200, verbose_name='المحقق')
    
    #12# الناشر
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الناشر")
    
    #13# طبعة سنة 
    print_year = models.CharField(verbose_name="سنة الطباعة", max_length=20)
   
    #14# طبعة رقم 
    print_number = models.CharField(verbose_name="رقم الطباعة", max_length=20)

    #15# مطبعة
    printing_house = models.ForeignKey(PrintingHouse, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المطبعة")


    #16# سنة النشر
    publish_year = models.CharField(verbose_name="سنة النشر", max_length=20)
    
    
    
    
    #17# ردمك الترجمة
    translation_isbn = models.CharField(
        verbose_name='ردمك الترجمة', max_length=50)

    #18# ردمد 
    issn = models.CharField(verbose_name='ردمد', max_length=50)

    #19# رقم الايداع
    deposit_number = models.CharField(
        verbose_name='رقم الايداع', max_length=60)

    # iso 
    iso = models.CharField(max_length=200)


    #20# فنان الغلاف 
    cover_artist = models.CharField(max_length=200, verbose_name="فنان الغلاف")
    
    #21# سلسلة 
    chain = models.CharField(max_length=100, verbose_name="السلسلة")

    #22# قسم
    branch = models.CharField(max_length=100, verbose_name="القسم")

    def __str__(self):
        return f"مترجم {self.mosannaf.name}"

    class Meta:
        verbose_name='مترجم مصنف'
        verbose_name_plural = "مترجمات المصنفات"