from orator import Model, SoftDeletes
from kink import di

Model.set_connection_resolver(di["db"])


class Student(Model, SoftDeletes):
    __table__ = "tbl_Aluno"