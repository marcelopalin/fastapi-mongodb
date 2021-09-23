from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    load_dotenv=True,
    dotenv_path="app/.env",
)

from pymongo import MongoClient
uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(settings.MONGO_ROOT_USER, settings.MONGO_ROOT_PASS, settings.MONGO_HOST, settings.MONGO_PORT, settings.MONGO_DB)
print(f"Connecting.. {settings.MONGODB_URI}")
client = MongoClient(uri)
conn = client['dev-db']
