from orator import Model
from kink import di


Model.set_connection_resolver(di["db"])


class Neuromuscular(Model):
    __table__ = "tbl_neuromuscular"
    __primary_key__= "id_neuromuscular"
    __timestamps__= False