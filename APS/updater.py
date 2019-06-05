from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from MarketPrices import Fetcher

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(Fetcher.updateDataD, 'interval', seconds=20)
    scheduler.start()