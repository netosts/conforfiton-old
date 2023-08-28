from kink import di
from orator import Model, SoftDeletes


Model.set_connection_resolver(di["db"])


class Personal(Model, SoftDeletes):
    __primary_key__ = "person_id"
    __timestamps__ = False
