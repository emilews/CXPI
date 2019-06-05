from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllMarketPrices),
    path('price/', views.getPrice),
]
