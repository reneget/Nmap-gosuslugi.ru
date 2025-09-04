import logging
from typing import Optional

import logging_loki


class LokiLogginHandler(logging_loki.LokiHandler):

    def __init__(
            self,
            url: str,
            tags: Optional[dict] = None,
            auth: Optional[tuple] = ('admin', 'admin'),
            version: str = "1"
    ):
        super().__init__(url=url, tags=tags, auth=auth, version=version)

    def emit(self, record: logging.LogRecord):
        try:
            self.emitter(record, self.format(record))
        except Exception as ex:
            self.handleError(record)
