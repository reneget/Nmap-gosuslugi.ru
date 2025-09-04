from dataclasses import dataclass
from typing import Optional


@dataclass
class LokiConfig:
    """
    Configuration class for Loki logger
    """
    url: str
    tags: Optional[dict] = None
    auth: Optional[tuple] = ('admin', 'admin')
    version: str = '1'


@dataclass
class DBConfig:
    """
    Configuration class for DataBase
    """
    db_url: str


@dataclass
class Config:
    """
    Main configuration class for whole project
    """
    loki: LokiConfig
    db: DBConfig
