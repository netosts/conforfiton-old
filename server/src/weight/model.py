from kink import di
from orator import Model, SoftDeletes


Model.set_connection_resolver(di["db"])


class Weight(Model, SoftDeletes):
    __timestamps__ = False
