from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class Redis:
    host: str
    port: int
    password: str


@dataclass
class ConfigEnv:
    tg_bot: TgBot
    redis: Redis

def load_config(path: str | None = None) -> ConfigEnv:
    env = Env()
    env.read_env(path)
    return ConfigEnv(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        redis=Redis(
            host=env('REDIS_HOST'),
            port=env('REDIS_PORT'),
            password=env('REDIS_PASSWORD'),
        ),
    )