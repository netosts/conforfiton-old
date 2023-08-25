from kink import di
from orator import Model, SoftDeletes
from orator.orm import morph_to


Model.set_connection_resolver(di["db"])


class User(Model, SoftDeletes):
    __primary_key__ = 'entity_id'
    __hidden__ = ["hash_password", "salt_password"]

    @morph_to
    def entity(self):
        return
