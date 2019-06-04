# CashX API Server
This server is created to parse the prices used originally by Bisq to fit the CashX needs.

## Why Django?
Django is an easy and understandable (maybe for a few?) framework for fast building web services and pages. Although Django REST Framework exists, it is too much of a hassle to deal with.

## How does it work?
It takes a request to the same endpoint that the Bisq ones use and hijacks it, then it asks for the real server and then parses it in a different way.
It strips the BTC price and uses BCH as base, then it calculates how much of a BCH the other coins are and modifies the JSON that came from the real server.

## How do I run it?
Clone this repo, then create a virtual environment with whatever tool you use, activate it and use
´´´
pip install -r requirements.txt
´´´
on the cloned folder.
Then just use
´´´
python manage.py migrate

python manage.py runserver
´´´
and that's all.

## License
Nah, just use it.