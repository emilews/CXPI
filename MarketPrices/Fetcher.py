from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse

import json

import requests

from bs4 import BeautifulSoup

# Global strings for original source
prefix = 'http://'
suffix = 'getAllMarketPrices/'

# Global URL for prices
BCH_Price_URL = 'https://coinmarketcap.com/currencies/bitcoin-cash/'
BTC_Price_URL = 'https://coinmarketcap.com/currencies/bitcoin/'

# Global variables
BCH_Price = 0
# Needed to get the price of the altcoins
BTC_Price = 0

# Global data
dataD = {}

# It updates the price on BTC and BCH, then it fetches the original JSON
# and changes the prices accordingly
def getAllMarketPrices():
  global dataD
  if dataD:
    return JsonResponse(dataD)
  else:
    return JsonResponse(updateDataD())

def getCMCPrice():
  global BCH_Price
  global BTC_Price
  r = requests.get(BCH_Price_URL)
  soup = BeautifulSoup(r.text, features="html.parser")
  req = soup.find_all('span', class_='h2 text-semi-bold details-panel-item--price__value')
  BCH_Price = float(req[0].string)
  print(BCH_Price)
  r = requests.get(BTC_Price_URL)
  soup = BeautifulSoup(r.text, features="html.parser")
  req = soup.find_all('span', class_='h2 text-semi-bold details-panel-item--price__value')
  BTC_Price = float(req[0].string)
  print(BTC_Price)


def parseJsonToBCH():
  global BCH_Price
  global BTC_Price
  global dataD
  for currency in dataD['data']:
    if currency['currencyCode'] == "BCH":
      currency['price'] = 1
    else:
      if currency['price'] > 1:
        newPrice = (BCH_Price * float(currency['price'])) / BTC_Price
        currency['price'] = newPrice
      else:
        USDPrice = (currency['price'] * BTC_Price)
        newPrice = (USDPrice / BCH_Price)
        currency['price'] = newPrice
  return dataD

def updateDataD():
  global dataD
  getCMCPrice()
  r = requests.get(prefix + '174.138.104.137:8080/' + suffix)
  if r.status_code == requests.codes.ok:
    dataD = r.json()
    return JsonResponse(parseJsonToBCH())
  else:
    return HttpResponseNotFound()