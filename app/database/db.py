from pymongo import MongoClient
from dynaconf import Dynaconf
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    load_dotenv=True,
    dotenv_path="app/.env",
)

if settings.DEBUG:
 print(f"Connecting.. {settings.MONGODB_URI}")
client = MongoClient(settings.MONGODB_URI)
conn = client[settings.MONGO_DB]
