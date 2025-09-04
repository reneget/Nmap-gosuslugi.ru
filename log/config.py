import os 

from configurations import main_config

config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standart': {
            'format': '%(levelname)s: %(message)s'
        },
        'debug': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        }
    },
    'handlers': {
        'grafana': {
            'class': 'log.custom_handlers.LokiLogginHandler',
            'url': main_config.loki.url,
            'tags': main_config.loki.tags,
            'auth':  main_config.loki.auth,
            'version':  main_config.loki.version,
            'formatter': 'debug',
            'level': 'DEBUG',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standart',
            'level': 'INFO',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers':{
        '': {
            'level': 'DEBUG',
            'handlers': ['grafana', 'console'],
            'propagate': False
        },
    }
}