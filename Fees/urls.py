from django.contrib import admin
from django.urls import path
from MarketPrices import views

urlpatterns = [
    path('', views.getFees),
]
