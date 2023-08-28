from kink import di
from orator import Model, SoftDeletes

Model.set_connection_resolver(di["db"])


class Company(Model, SoftDeletes):
    __table__ = "companies"
