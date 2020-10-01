from django.db import models


class TaskO(models.Model):
    choice = (
        ('1', '1 звезда'),
        ('2', '2 звезды'),
        ('3', '3 звезды'),
        ('4', '4 звезды'),
        ('5', '5 звезд'),
    )
    title = models.CharField('Название', max_length=28)
    price = models.IntegerField('Цена', null=True)
    description = models.TextField('Описания задания', null=True)
    task = models.CharField('Вид поездки', max_length=90)
    data = models.DateField(null=True)
    image = models.ImageField(upload_to='BD/', null=True)
    stars = models.CharField('Количевство звезд отеля', max_length=2, choices=choice, null=True)
    country = models.CharField("Страна", max_length=40, null=True)

    def __str__(self):
        return self.title

