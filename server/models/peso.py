from orator import Model
from kink import di


Model.set_connection_resolver(di["db"])


class Peso(Model):
    __table__ = "tbl_peso"
    __primary_key__="ID_peso"
    __timestamps__=False