# STARTING

We will construct API with FastAPI and MongoDB

# Step 1

Create project com poetry:

```s
poetry init
```

If you are using zsh do:
```s
poetry add fastapi\[all\]
```
from bash:
```s
poetry add fastapi[all]
```

```s
poetry add dynaconf loguru requests
poetry add pymongo
```

Problems: if you installed uvicorn or jinja2 before fastapi[all]
you should remove and then install fastapi.


To see instaled packages type: `poetry show`


# Step 2

Initialize Dynacon on your project.

```
poetry shell
dynaconf init -f toml
```

```s
 Configuring your Dynaconf environment
------------------------------------------
🐍 The file `config.py` was generated.
  on your code now use `from config import settings`.
  (you must have `config` importable in your PYTHONPATH).

🎛️  settings.toml created to hold your settings.

🔑 .secrets.toml created to hold your secrets.

🙈 the .secrets.toml is also included in `.gitignore` 
  beware to not push your secrets to a public repo 
  or use dynaconf builtin support for Vault Servers.

🎉 Dynaconf is configured! read more on https://dynaconf.com
   Use `dynaconf -i config.settings list` to see your settings
```

This will create `.secrets.toml` `config.py` and `settings.toml`

Use `dynaconf -i config.settings list` to see your settings:

```s
DEFAULT<dict> {'APP_DESCRIPTION': 'API with MongoDB! 🇧🇷',
 'APP_NAME': 'API FastAPI! 🚀',
 'APP_VERSAO': '1.0.0',
 'CURRENT_ENV': 'main',
 'DEBUG': False,
 'DIR_INPUT': 'Entrada',
 'DIR_OUTPUT': 'Saida',
 'HOME_DIR': '/home/mpi',
 'URL_CHECK_PUBLIC_IP': 'https://ifconfig.me'}
DEVELOPMENT<dict> {'RUN_S00': False}
PRODUCTION<dict> {'RUN_S00': True}
```

# How to Create DockerFile wih VSCode

https://towardsdatascience.com/the-nice-way-to-use-docker-with-vscode-f475c49aab1b

`Ctrl + Shift + P`  

Create requirements.txt from poetry:

```s
poetry export -f requirements.txt -o requirements.txt --without-hashes
```

```s
docker build --rm --pull -f "/home/mpi/github.com/fastapi-mongodb/Dockerfile" --label "com.microsoft.created-by=visual-studio-code" -t "fastapimongodb:latest"
```

```s
docker run --rm -d  -p 8000:8000 fastapimongodb:latest
```

Create `.env` file:

```s
export ENV_FOR_DYNACONF=development # development ou production
export DYANCONF_CONFIG_BASICAUTH_USERNAME="mongo_user"
export DYANCONF_CONFIG_BASICAUTH_PASSWORD="pass123"
export DYANCONF_CONFIG_MONGODB_PORT=27017
export DYANCONF_CONFIG_MONGODB_ADMINUSERNAME="root"
export DYANCONF_CONFIG_MONGODB_ADMINPASSWORD="Mongodb2021"
```

In your real project put this values on `.secrets.toml`

Start Docker MongoDb and MongoExpress:

```s
docker-compose -f docker-compose-mongo.yml up -d
```

You can access at `http://localhost:8081` mongo-express. 
Put your DYANCONF_CONFIG_BASICAUTH_USERNAME and DYANCONF_CONFIG_BASICAUTH_PASSWORD.

# How to connect Docker MongoDB

```
docker exec -it mongo /bin/bash
```



# Refs

https://medium.com/fastapi-tutorials/integrating-fastapi-and-mongodb-8ef4f2ca68ad

https://towardsdatascience.com/the-nice-way-to-use-docker-with-vscode-f475c49aab1b

https://www.mongodb.com/developer/quickstart/python-quickstart-fastapi/

https://testdriven.io/blog/fastapi-mongo/

https://medium.com/rahasak/enable-mongodb-authentication-with-docker-1b9f7d405a94


https://medium.com/1mgofficial/how-to-override-uvicorn-logger-in-fastapi-using-loguru-124133cdcd4e
