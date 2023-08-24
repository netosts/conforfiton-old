from orator import Model, SoftDeletes
from kink import di


Model.set_connection_resolver(di["db"])


class Person(Model, SoftDeletes):
    pass
