
import os
from dataclasses import dataclass
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

@dataclass(frozen=True)
class Config:
    ENV: str = os.getenv('ENV', 'development')
    DEBUG: bool = os.getenv('DEBUG', True)
    APP_HOST: str = os.getenv('APP_HOST', '0.0.0.0')
    APP_PORT: str = os.getenv('APP_PORT', 8000)
    DB_USER: str = os.getenv('DB_USER', 'postgress')
    DB_PASS: str = os.getenv('DB_PASS', 'postgress')
    DB_HOST: str = os.getenv('DB_HOST', 'db')
    DB_NAME: str = os.getenv('DB_NAME', 'web_db')
    DB_URL: str = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'random')
    JWT_ALGORITHM = 'HS256'
    SENTRY_SDN: str = os.getenv('SENTRY_DSN')


@dataclass(frozen=True)
class DevelopmentConfig(Config):
    DEBUG = True


@dataclass(frozen=True)
class TestingConfig(Config):
    DEBUG = True


@dataclass(frozen=True)
class ProductionConfig(Config):
    DEBUG = False


def get_config():
    env = os.getenv('ENV', 'development')
    config_type = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig
    }
    return config_type[env]
