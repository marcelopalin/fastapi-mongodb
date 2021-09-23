import sys
from fastapi import FastAPI
import uvicorn
from pathlib import Path
from app.config import settings
import logging
from app.src.custom_logging import CustomizeLogger

from app.routes.user import router

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from loguru import logger
# logger.remove()
# logger.add(sys.stdout, colorize=True, format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>")

logger = logging.getLogger(__name__)
config_path=Path(__file__).with_name("logging_config.json")
logger.setLevel(logging.DEBUG)


from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    load_dotenv=True,
)


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSAO,
        default_response_class=ORJSONResponse,
        debug=settings.DEBUG
    )
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    return app


app = create_app()
app.include_router(router)

if __name__ == '__main__':
      uvicorn.run(app, port=8009)