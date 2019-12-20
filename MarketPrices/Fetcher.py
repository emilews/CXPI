from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse

import json

import requests

from bs4 import BeautifulSoup

# Global strings for original source
prefix = 'http://'
suffixPrices = 'getAllMarketPrices/'
suffixFees = 'getFees/'

# Global URL for prices
BCH_Price_URL = 'https://coinmarketcap.com/currencies/bitcoin-cash/'
BTC_Price_URL = 'https://coinmarketcap.com/currencies/bitcoin/'

# Global variables
BCH_Price = 0
# Needed to get the price of the altcoins
BTC_Price = 0

# Global data
dataD = {}
feesData = {}


# It updates the price on BTC and BCH, then it fetches the original JSON
# and changes the prices accordingly
def getAllMarketPrices():
  global dataD
  if dataD:
    return JsonResponse(dataD)
  else:
    return JsonResponse(updateDataD())

def getFees():
  global feesData
  if feesData:
    return JsonResponse(feesData)
  else:
    temp = updateDataD()
    return JsonResponse(feesData)

def getCMCPrice():
  global BCH_Price
  global BTC_Price
  r = requests.get(BCH_Price_URL)
  soup = BeautifulSoup(r.text, features="html.parser")
  req = soup.find_all('span', class_='cmc-details-panel-price__price')
  BCH_Price = float(req[0].string.split('$')[1])
  print(BCH_Price)
  r = requests.get(BTC_Price_URL)
  soup = BeautifulSoup(r.text, features="html.parser")
  req = soup.find_all('span', class_='cmc-details-panel-price__price')
  BTC_Price = float(req[0].string.split('$')[1].replace(',',''))
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
  global feesData
  getCMCPrice()
  r = requests.get(prefix + '174.138.104.137:8080/' + suffixPrices)
  fees = requests.get(prefix + '174.138.104.137:8080/' + suffixFees)
  feesData = fees.json()
  if r.status_code == requests.codes.ok:
    dataD = r.json()
    return JsonResponse(parseJsonToBCH())
  else:
    return HttpResponseNotFound()