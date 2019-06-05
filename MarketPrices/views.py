from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse

import requests

from . import Fetcher
# Global variable for requests
prefix = 'http://'
suffix = 'getAllMarketPrices/'

# This is the base method, as you can see, is fetching the JSON from 
# the original source
def getAllMarketPrices(request):
  if request.method == 'GET':
    data = Fetcher.getAllMarketPrices()
    if data:
      return data
    else:
      return HttpResponseNotFound()

def getPrice(request):
  Fetcher.getCMCPrice()  
  return HttpResponseNotFound()