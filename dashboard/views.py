from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse
from .models import BCHData

# Create your views here.

def getDashboard(request):
    return HttpResponseNotFound()

def getBCHPrice(request):
    if request.method == 'GET':
        latest = BCHData.objects.latest('date_of_price')
        price = latest.price
        return JsonResponse(price, safe=False)