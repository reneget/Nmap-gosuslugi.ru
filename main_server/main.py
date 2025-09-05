from fastapi import FastAPI
import uvicorn

import logging

from API import server_router
from log import config

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

logging.config.dictConfig(config)
main_log = logging.getLogger(__name__)

app = FastAPI()
main_log.info('FastAPI object initialized')

main_log.info('Connecting routers')
app.include_router(server_router)
main_log.info('Routers are connected')
