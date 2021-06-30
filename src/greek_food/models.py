from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone, dateformat



# Create your models here.


class Cafe(models.Model):
    name = models.CharField(max_length=64)


class CafePlaces(models.Model):
    cafe = models.ForeignKey(to=Cafe, related_name='cafe_places', on_delete=models.CASCADE)
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)

    @property
    def square(self):
        return self.width * self.height


class TableInfo(models.Model):
    MAX_LIMIT = 100
    width = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                         MaxValueValidator(MAX_LIMIT)], default=0)
    height = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                          MaxValueValidator(MAX_LIMIT)], default=0)
    x = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(MAX_LIMIT)], default=0)
    y = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(MAX_LIMIT)], default=0)

    def right(self):
        return self.x + self.width

    def bottom(self):
        return self.y + self.height

    def square(self):
        return self.right() * self.bottom()


class Table(TableInfo):
    SHAPE_CHOICES = (
        ("rectangular", 'Rectangular'),
        ("oval", 'Oval'),
    )
    place = models.ForeignKey(to=CafePlaces, related_name='tables', on_delete=models.CASCADE, default=0)
    number = models.PositiveSmallIntegerField()
    number_of_seats = models.PositiveSmallIntegerField(default=0)
    shape = models.CharField(choices=SHAPE_CHOICES, max_length=64)

    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number} - {self.shape}'

    def is_reserve(self, current_date):
        is_exists = self.orders.filter(start_date__lte=current_date, end_date__gte=current_date).exists()
        self.is_reserved = True if is_exists else False
        self.save()


class Customer(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, related_name='orders', on_delete=models.CASCADE)


class OrderDetail(models.Model):
    order = models.ForeignKey(to=Order, related_name='order_details', on_delete=models.CASCADE)
    table = models.ForeignKey(to=Table, related_name='order_details', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)




