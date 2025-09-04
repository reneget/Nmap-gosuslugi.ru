from . import config as cf
from .env_conf import EnvConfig

main_config = cf.Config(
    loki=cf.LokiConfig(
        url=EnvConfig.read()('LOKI_URL')
    ),
    db=cf.DBConfig(
        db_url=EnvConfig.read()('DATABASE_URL')
    )
)
