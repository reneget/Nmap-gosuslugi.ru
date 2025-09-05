from dataclasses import dataclass
from typing import Optional


@dataclass
class LokiConfig:
    url: str
    tags: Optional[dict] = None
    auth: Optional[tuple] = ('admin', 'admin')
    version: str = '1'


@dataclass
class Config:
    loki: LokiConfig