from kink import di
from orator import Model


Model.set_connection_resolver(di["db"])


class Weight(Model):
    __timestamps__ = False
