from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

import logging

import API
from DataBase.core.db_connection import create_tables
from log import config

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

logging.config.dictConfig(config)
main_log = logging.getLogger(__name__)

main_log.info('Creating Tables')
create_tables()
main_log.info('Tables created')

app = FastAPI()
main_log.info('FastAPI object initialized')

main_log.info('Connecting routers')
app.include_router(API.user_router)
main_log.info('Routers are connected')

