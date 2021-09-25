import os
from pymongo import MongoClient
from dynaconf import Dynaconf
import motor.motor_asyncio
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    load_dotenv=True,
    dotenv_path="app/.env",
)


client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URI)
db = client[settings.MONGO_DB]

if settings.DEBUG:
 print(f"Connecting.. {settings.MONGODB_URI}")

