from django.apps import AppConfig


class MarketpricesConfig(AppConfig):
    name = 'MarketPrices'

    def ready(self):
        from APS import updater
        updater.start()