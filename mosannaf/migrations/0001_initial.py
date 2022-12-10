# Generated by Django 4.1.3 on 2022-12-07 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="اسم النشاط")),
            ],
            options={
                "verbose_name": "نشاط",
                "verbose_name_plural": "الأنشطة",
            },
        ),
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="القسم")),
            ],
            options={
                "verbose_name": "قسم",
                "verbose_name_plural": "اﻷقسام",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="فئة المصنف")),
            ],
            options={
                "verbose_name": "فئة المصنف",
                "verbose_name_plural": "فئات المصنفات",
            },
        ),
        migrations.CreateModel(
            name="Field",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="اسم المجال")),
            ],
            options={
                "verbose_name": "مجال",
                "verbose_name_plural": "المجالات",
            },
        ),
        migrations.CreateModel(
            name="Lang",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="اللغة")),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="الاسم")),
                ("country", models.CharField(max_length=150, verbose_name="الدولة")),
                ("territory", models.CharField(max_length=100, verbose_name="إقليم")),
                ("county", models.CharField(max_length=100, verbose_name="مقاطعة")),
                ("region", models.CharField(max_length=100, verbose_name="منطقة")),
                ("city", models.CharField(max_length=100, verbose_name="مدينة")),
                (
                    "governorate",
                    models.CharField(max_length=100, verbose_name="محافظة"),
                ),
                ("village", models.CharField(max_length=100, verbose_name="قرية")),
                ("neighborhood", models.CharField(max_length=100, verbose_name="حي")),
                ("street", models.CharField(max_length=100, verbose_name="شارع")),
                ("building", models.IntegerField(default=0, verbose_name="بناية رقم")),
                ("floor", models.IntegerField(default=0, verbose_name="الدور")),
                ("unit", models.CharField(max_length=20, verbose_name="الوحدة")),
                (
                    "nearest_landmark",
                    models.CharField(max_length=150, verbose_name="أقرب معلم بارز"),
                ),
                (
                    "coordinates",
                    models.CharField(max_length=100, verbose_name="إحداثيات"),
                ),
                (
                    "landline_number",
                    models.CharField(max_length=20, verbose_name="هاتف رقم"),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=20, verbose_name="جوال رقم"),
                ),
                (
                    "fax_number",
                    models.CharField(max_length=25, verbose_name="فاكس رقم"),
                ),
                ("telex", models.CharField(max_length=50, verbose_name="تلكس")),
                ("pobox", models.CharField(max_length=50, verbose_name="صندوق بريد")),
                (
                    "postal_code",
                    models.CharField(max_length=50, verbose_name="الرمز البريدي"),
                ),
                (
                    "email",
                    models.EmailField(max_length=150, verbose_name="البريد الإلكتروني"),
                ),
            ],
            options={
                "verbose_name": "ناشر",
                "verbose_name_plural": "الناشرون",
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="موضوع")),
            ],
            options={
                "verbose_name": "موضوع",
                "verbose_name_plural": "المواضيع",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="نوع المصنف")),
            ],
            options={
                "verbose_name": "نوع المصنف",
                "verbose_name_plural": "أنوع المصنفات",
            },
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="باب")),
            ],
            options={
                "verbose_name": "باب",
                "verbose_name_plural": "الأبواب",
            },
        ),
        migrations.CreateModel(
            name="SubBranch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="القسم الفرعي")),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mosannaf.branch",
                        verbose_name="القسم",
                    ),
                ),
            ],
            options={
                "verbose_name": "قسم الفرعي",
                "verbose_name_plural": "اﻷقسام الفرعية",
            },
        ),
        migrations.CreateModel(
            name="Mosannaf",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="اسم المصنف")),
                ("meaning", models.TextField(verbose_name="تفسير اسم المصنف")),
                ("date_published", models.DateField(verbose_name="تاريخ النشر")),
                ("parts_count", models.IntegerField(default=0, verbose_name="الأجزاء")),
                ("pages_count", models.IntegerField(default=0, verbose_name="الصفحات")),
                ("units_count", models.IntegerField(default=0, verbose_name="اﻷبواب")),
                (
                    "chapters_count",
                    models.IntegerField(default=0, verbose_name="الفصول"),
                ),
                ("summary", models.TextField(verbose_name="نبذه عن المصنف")),
                (
                    "image",
                    models.ImageField(upload_to="أغلفة/", verbose_name="صورة المصنف"),
                ),
                (
                    "file",
                    models.FileField(upload_to="مصنفات/", verbose_name="ملف المصنف"),
                ),
                (
                    "activity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.activity",
                        verbose_name="النشاط",
                    ),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.branch",
                        verbose_name="القسم",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.category",
                        verbose_name="فئة المصنف",
                    ),
                ),
                (
                    "field",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.field",
                        verbose_name="المجال",
                    ),
                ),
                (
                    "m_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.type",
                        verbose_name="نوع المصنف",
                    ),
                ),
                (
                    "original_lang",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.lang",
                        verbose_name="أصل لغة المصنف",
                    ),
                ),
                (
                    "sub_branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.subbranch",
                        verbose_name="القسم الفرعي",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.subject",
                        verbose_name="الموضوع",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mosannaf.unit",
                        verbose_name="باب",
                    ),
                ),
            ],
            options={
                "verbose_name": "مصنف",
                "verbose_name_plural": "المصنفات",
            },
        ),
    ]
