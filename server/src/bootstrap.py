import yaml
from kink import di
from orator import DatabaseManager
from os import path

# Get current directory "conforfit-db\\server\\src\\"
script_dir = path.dirname(path.abspath(__file__))
# Make a path for Windows and Linux based on current directory
config_path = path.join(script_dir, "..", "etc", "config.yaml")


def bootstrap():

    with open(config_path, 'r', encoding="UTF-8") as folder:
        config = yaml.safe_load(folder)  # safe_load because load is deprecated
        di["config"] = config

        # connect to the database
        db = DatabaseManager(di["config"]["databases"])
        di["db"] = db

    # JWT Auth injections
    di["SECRET_KEY"] = config["SECRET_KEY"]
    di["ALGORITHM"] = config["ALGORITHM"]
    di["ACCESS_TOKEN_EXP"] = config["ACCESS_TOKEN_EXPIRE_MINUTES"]
    # Cors Middleware ORIGINS
    di["ORIGINS"] = config["ORIGINS"]
