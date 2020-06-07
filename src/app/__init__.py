import uvicorn
from fastapi import FastAPI
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from dotenv import load_dotenv
from starlette.requests import Request

from app.routes import home_router
from app.routes.v1 import orders_router
from core.config import get_config
from core.exception import CustomException

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()


def init_routers(app: FastAPI) -> None:
    app.include_router(home_router)
    app.include_router(orders_router, prefix='/api/v1', tags=['Orders'])

def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return dict(
            status_code=exc.code,
            content=exc.kwargs,
        )

def create_app() -> FastAPI:
    config = get_config()
    app = FastAPI(
        title='Hide',
        description='Hide API',
        version='1.0.0',
        docs_url=None if config.ENV == 'production' else '/docs',
        redoc_url=None if config.ENV == 'production' else '/redoc',
    )
    init_routers(app=app)
    init_listeners(app=app)
    app.add_middleware(DBSessionMiddleware, db_url=config.DB_URL)

    return app


app = create_app()
