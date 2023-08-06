from orator import Model
from kink import di


Model.set_connection_resolver(di["db"])


class Cardio(Model):
    __table__ = "tbl_fq_cardio"
    __primary_key__= "id_fq_cardio"
    __timestamps__= False