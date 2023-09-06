from kink import di
from orator import Model, SoftDeletes


Model.set_connection_resolver(di["db"])


class Antropometria(Model, SoftDeletes):
    __timestamps__ = False
