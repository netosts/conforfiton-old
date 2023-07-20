from orator import Model, SoftDeletes
from kink import di


Model.set_connection_resolver(di["db"])


class Auth(Model, SoftDeletes):
    __table__ = "tbl_Auth"
    __primary_key__= "ID_Pessoa"