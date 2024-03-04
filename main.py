from fastapi import FastAPI
from routes import routes
from apscheduler.schedulers.background import BackgroundScheduler
from core.async_session import get_async_session

app = FastAPI()


# @app.on_event('startup')
# def init_data():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(make_request_to_api_currency, 'cron', second='*/1', args=(get_async_session,))
#     scheduler.start()


app.include_router(routes)
