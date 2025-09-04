from environs import Env

from typing import Any


class EnvConfig:
    @staticmethod
    def read():
        env = Env()
        env.read_env()

        return env
