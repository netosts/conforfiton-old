import yaml
from kink import di
from orator import DatabaseManager
import os.path as opath


def bootstrap():
    file = opath.join('etc', 'config.yaml')

    with open(f"{file}", 'r', encoding="UTF-8") as folder:
        config = yaml.safe_load(folder)  # safe_load because load is deprecated
        di["config"] = config

        # connect to the database
        db = DatabaseManager(di["config"]["databases"])
        di["db"] = db

    di["SECRET_KEY"] = config["SECRET_KEY"]
    di["ALGORITHM"] = config["ALGORITHM"]
    di["ACCESS_TOKEN_EXP"] = config["ACCESS_TOKEN_EXPIRE_MINUTES"]

    di["ORIGINS"] = config["ORIGINS"]
