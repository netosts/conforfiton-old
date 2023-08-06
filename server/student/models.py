from orator import Model
from kink import di


Model.set_connection_resolver(di["db"])


class Student(Model):
    __table__ = "tbl_aluno"
    __primary_key__= "id_pessoa"
    __timestamps__ = False