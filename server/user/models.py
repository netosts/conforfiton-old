from orator import Model, SoftDeletes
from kink import di


Model.set_connection_resolver(di["db"])


class User(Model, SoftDeletes):
    __table__ = "tbl_auth"
    __primary_key__= "id_pessoa"
    __hidden__ = ["hash", "salt"]