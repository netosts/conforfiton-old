import yaml
from kink import di
from orator import DatabaseManager


def bootstrap():

    with open('../etc/config.yaml', 'r', encoding='UTF-8') as folder:
        config = yaml.safe_load(folder)
        di["config"] = config

        db = DatabaseManager(di["config"]["databases"])
        di["db"] = db
