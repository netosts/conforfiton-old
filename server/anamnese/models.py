from orator import Model, SoftDeletes
from kink import di


Model.set_connection_resolver(di["db"])


class Anamnese(Model, SoftDeletes):
    __primary_key__ = "person_id"
