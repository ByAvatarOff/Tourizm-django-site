# Generated by Django 3.0.5 on 2020-09-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=70, verbose_name='Эмэйл адрес')),
                ('nickname', models.CharField(max_length=60, verbose_name='Никнейм')),
                ('password', models.TextField(verbose_name='Пароль')),
                ('city', models.CharField(max_length=60, verbose_name='Город проживания')),
                ('date', models.DateField(verbose_name='Дата рождения')),
            ],
        ),
        migrations.AlterModelOptions(
            name='tasko',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
