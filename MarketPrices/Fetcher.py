from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse

import requests

from bs4 import BeautifulSoup



# Global variable for requests
prefix = 'http://'
suffix = 'getAllMarketPrices/'
BCH_Price_URL = 'https://coinmarketcap.com/currencies/bitcoin-cash/'

# Global variables
BCH_Price = 0

# This is the base method, as you can see, is fetching the JSON from 
# the original source
def getAllMarketPrices():
  r = requests.get(prefix + '174.138.104.137:8080/'+suffix)
  if r.status_code == requests.codes.ok:
    return JsonResponse(r.json())
  else:
    return HttpResponseNotFound()

def getCMCPrice():
  global BCH_Price
  r = requests.get(BCH_Price_URL)
  soup = BeautifulSoup(r.text, features="html.parser")
  req = soup.find_all('span', class_='h2 text-semi-bold details-panel-item--price__value')
  BCH_Price = req[0].string
  print('New BCH price: ' + BCH_Price)
  