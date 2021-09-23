#!/bin/zsh
# Install pre-commit
poetry run pre-commit install
# https://phoenixnap.com/kb/create-directory-linux-mkdir-command

dir1=$HOME/.docker/database/dump_mongodb
dir2=$HOME/.docker/database/mongodb
echo "Created $dir1 and $dir2 to store docker volumes!"
mkdir -p $HOME/.docker/database/{dump_mongodb,mongodb}
