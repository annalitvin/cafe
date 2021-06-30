from django.urls import path

from . import views

app_name = 'greek_food'

urlpatterns = [
    path('list', views.TableListView.as_view(), name='list'),
    path('reserved/<int:pk>', views.ReservedView.as_view(), name='reserved'),
]
