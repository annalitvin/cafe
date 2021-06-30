from datetime import timezone

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy

# Create your views here.
from greek_food.models import Table, Order, Customer, OrderDetail
from greek_food.forms import OrderForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, FormView

from django.http import HttpResponse, Http404

import datetime

from app import settings
from greek_food.forms import DateForm


class TableListView(ListView):
    model = Table
    template_name = 'greek_food/table_list.html'
    context_object_name = 'table_list'

    def get_queryset(self):
        date = self.request.GET.get('date')
        qs = super().get_queryset()

        if date:
            datetime_object = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
            for i in qs:
                i.is_reserve(datetime_object)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = DateForm()
        context['title'] = 'LeaderBoard'
        return context


class ReservedView(CreateView):
    model = OrderDetail
    template_name = 'greek_food/reserved.html'
    extra_context = {'title': 'Send us a message!'}
    success_url = reverse_lazy('greek_food:list')
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        table_id = self.kwargs.get(self.pk_url_kwarg)

        if form.is_valid():
            customer = Customer.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            table = Table.objects.get(pk=table_id)
            order = Order.objects.get(customer=customer)
            self.object = form.save(commit=False)
            self.object.order = order
            self.object.table = table
            self.object.save()

            send_mail(
                 subject=f"Столик # {table_id} заказан",
                 message=f"Заказ успешен от {self.object.start_date} до {self.object.end_date}",
                 from_email=settings.EMAIL_HOST_USER,
                 recipient_list=[form.cleaned_data['email']],
                 fail_silently=False,
             )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




















# class IndexTableDetailView(DetailView):
#     model = Table
#     template_name = 'group/index.html'
#     context_object_name = 'group'
#
#     def get_object(self, queryset=None):
#         pass
#
#         # id_group = self.kwargs.get(self.pk_url_kwarg)
#         # try:
#         #     group_obj = self.model.objects.get(pk=id_group)
#         # except self.model.DoesNotExist:
#         #     raise Http404("Group does not exist")
#         # return group_obj
#
#     def get(self, request, *args, **kwargs):
#         pass
#
#         # id_group = self.kwargs.get(self.pk_url_kwarg)
#         # if id_group is not None:
#         #     if id_group == 0:
#         #         return HttpResponse("'id' must be greatest when zero")
#
#         return super().get(request, *args, **kwargs)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=None, **kwargs)
#         context['title'] = 'Group'
#         return context
