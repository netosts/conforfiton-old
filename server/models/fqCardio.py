from orator import Model
from kink import di


Model.set_connection_resolver(di["db"])


class fqCardio(Model):
    __table__ = "tbl_fqCardio"
    __primary_key__= "ID_fqCardio"
    __timestamps__= False