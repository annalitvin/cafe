from django.forms import Form, fields
from django.views.generic import FormView
from django import forms
from django.forms import ModelForm
from greek_food.models import Table, Order, Customer, OrderDetail

from datetimewidget.widgets import DateTimeWidget

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderForm(ModelForm):
    name = forms.CharField(label=("Name", ))
    email = forms.EmailField(label=("E-mail",))
    class Meta:
        model = OrderDetail
        fields = ['name', 'email', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
        }


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )



