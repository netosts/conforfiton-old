from orator import Model
from kink import di


Model.set_connection_resolver(di["db"])


class Anamnese(Model):
    __table__ = "tbl_anamnese"
    __primary_key__= "id_pessoa"