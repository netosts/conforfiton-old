from orator import Model
from kink import di


Model.set_connection_resolver(di["db"])


class Student(Model):
    __table__ = "tbl_Aluno"
    __primary_key__= "ID_Pessoa"
    __timestamps__ = False