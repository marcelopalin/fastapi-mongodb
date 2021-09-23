if [ -f settings.toml ]; then
    echo "settings.toml exists!"
else
    echo "settings.toml does not exist!"
    cp settings_example.toml settings.toml 
    echo "settings.toml created using settings_example.toml!"
    exit 1
fi

EXAMPLE_SETTINGS=$(cat settings_example.toml)
SETTINGS=$(cat settings.toml)

if [ "$EXAMPLE_SETTINGS" = "$SETTINGS" ]; then
    echo "settings_example.toml is UP TO DATE!"
    exit 0
else
    echo "Updating settings_example.toml from settings.toml!"
    cp settings.toml settings_example.toml
    exit 1
fi
