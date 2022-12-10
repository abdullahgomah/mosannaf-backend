# Generated by Django 4.1.3 on 2022-12-08 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mosannaf", "0007_delete_publisher"),
    ]

    operations = [
        migrations.AddField(
            model_name="mosannaf",
            name="measurement",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mosannaf.measurement",
                verbose_name="قياس المصنف",
            ),
        ),
    ]
