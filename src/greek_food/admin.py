from django.contrib import admin

# Register your models here.
from greek_food.models import Table, CafePlaces, Cafe, Order, Customer

admin.site.register(Table)
admin.site.register(CafePlaces)
admin.site.register(Cafe)
admin.site.register(Order)
admin.site.register(Customer)
