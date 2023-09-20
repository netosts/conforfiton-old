from kink import di
from orator import Model, SoftDeletes


Model.set_connection_resolver(di["db"])


class User(Model, SoftDeletes):
    __primary_key__ = 'person_id'
    __hidden__ = ["hash_password", "salt_password"]
