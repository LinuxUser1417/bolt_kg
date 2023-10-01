from django.urls import path
from . import views

urlpatterns = [
    path('', views.bolt_sales, name='bolt_sales'),
]
