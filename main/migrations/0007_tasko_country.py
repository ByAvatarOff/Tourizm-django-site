# Generated by Django 3.0.5 on 2020-09-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200920_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasko',
            name='country',
            field=models.CharField(max_length=40, null=True, verbose_name='Страна'),
        ),
    ]
